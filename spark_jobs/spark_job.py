# from pyspark.sql import SparkSession
# from pyspark.sql.functions import col, avg, lit, when

# # إعداد Spark مع إعدادات MinIO
# spark = SparkSession.builder \
#     .appName("StudentDataProcessing") \
#     .config("spark.hadoop.fs.s3a.endpoint", "http://minio:9000") \
#     .config("spark.hadoop.fs.s3a.access.key", "admin") \
#     .config("spark.hadoop.fs.s3a.secret.key", "password") \
#     .config("spark.hadoop.fs.s3a.path.style.access", "true") \
#     .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
#     .getOrCreate()

# # قراءة الملفات من MinIO
# df1 = spark.read.csv("s3a://student-data/Students_Grading_Dataset.csv", header=True, inferSchema=True)
# df2 = spark.read.csv("s3a://student-data/student_performance_large_dataset.csv", header=True, inferSchema=True)
# df3 = spark.read.csv("s3a://student-data/education_career_success.csv", header=True, inferSchema=True)

# # إضافة عمود "Source"
# df1 = df1.withColumn("Source", lit("Grading"))
# df2 = df2.withColumn("Source", lit("Performance"))
# df3 = df3.withColumn("Source", lit("Career"))

# # حساب Success_Rate بناءً على البيانات المتاحة
# df1 = df1.withColumn("Success_Rate", when(col("Total_Score").isNotNull(), col("Total_Score") / 100).otherwise(0))
# df2 = df2.withColumn("Success_Rate", when(col("Exam_Score (%)").isNotNull(), col("Exam_Score (%)") / 100).otherwise(0))
# df3 = df3.withColumn("Success_Rate", when(col("University_GPA").isNotNull(), col("University_GPA") / 4).otherwise(0))  # تحويل GPA لنسبة

# # الـ schema المشترك المعدل
# from pyspark.sql.types import StructType, StructField, StringType, DoubleType
# common_schema = StructType([
#     StructField("Student_ID", StringType(), True),
#     StructField("Department", StringType(), True),
#     StructField("Success_Rate", DoubleType(), True),
#     StructField("Source", StringType(), True)
# ])

# # تحويل الأطر إلى الـ schema المشترك
# df1_adjusted = df1.select(
#     col("Student_ID").cast(common_schema["Student_ID"].dataType),
#     col("Department").cast(common_schema["Department"].dataType),
#     col("Success_Rate").cast(common_schema["Success_Rate"].dataType),
#     col("Source").cast(common_schema["Source"].dataType)
# )
# df2_adjusted = df2.select(
#     col("Student_ID").cast(common_schema["Student_ID"].dataType),
#     lit(None).cast(common_schema["Department"].dataType).alias("Department"),
#     col("Success_Rate").cast(common_schema["Success_Rate"].dataType),
#     col("Source").cast(common_schema["Source"].dataType)
# )
# df3_adjusted = df3.select(
#     col("Student_ID").cast(common_schema["Student_ID"].dataType),
#     col("Field_of_Study").cast(common_schema["Department"].dataType).alias("Department"),
#     col("Success_Rate").cast(common_schema["Success_Rate"].dataType),
#     col("Source").cast(common_schema["Source"].dataType)
# )

# # دمج البيانات
# merged_df = df1_adjusted.union(df2_adjusted).union(df3_adjusted)

# # حفظ الأطر في PostgreSQL
# df1_adjusted.write \
#     .format("jdbc") \
#     .option("url", "jdbc:postgresql://postgres:5432/student_db") \
#     .option("dbtable", "grading_data") \
#     .option("user", "user") \
#     .option("password", "password") \
#     .option("driver", "org.postgresql.Driver") \
#     .mode("overwrite") \
#     .save()

# df2_adjusted.write \
#     .format("jdbc") \
#     .option("url", "jdbc:postgresql://postgres:5432/student_db") \
#     .option("dbtable", "performance_data") \
#     .option("user", "user") \
#     .option("password", "password") \
#     .option("driver", "org.postgresql.Driver") \
#     .mode("overwrite") \
#     .save()

# df3_adjusted.write \
#     .format("jdbc") \
#     .option("url", "jdbc:postgresql://postgres:5432/student_db") \
#     .option("dbtable", "career_data") \
#     .option("user", "user") \
#     .option("password", "password") \
#     .option("driver", "org.postgresql.Driver") \
#     .mode("overwrite") \
#     .save()

# # تحليل وتحديث جدول department_scores
# result = merged_df.groupBy("Department").agg(avg("Success_Rate").alias("Avg_Success_Rate"))
# result.write \
#     .format("jdbc") \
#     .option("url", "jdbc:postgresql://postgres:5432/student_db") \
#     .option("dbtable", "department_scores") \
#     .option("user", "user") \
#     .option("password", "password") \
#     .option("driver", "org.postgresql.Driver") \
#     .mode("overwrite") \
#     .save()

# result.show()

# spark.stop()

from pyspark.sql import SparkSession
from pyspark.sql.functions import lit

# إنشاء Spark Session
spark = SparkSession.builder \
    .appName("StudentDataProcessing") \
    .config("spark.jars", "/tmp/spark_jobs/lib/postgresql-42.7.3.jar") \
    .getOrCreate()

# قراءة الملفات من MinIO
df_grading = spark.read.csv("s3a://student-data/Students_Grading_Dataset.csv", header=True, inferSchema=True)
df_performance = spark.read.csv("s3a://student-data/student_performance_large_dataset.csv", header=True, inferSchema=True)
df_career = spark.read.csv("s3a://student-data/education_career_success.csv", header=True, inferSchema=True)

# إضافة عمود Source
df_grading = df_grading.withColumn("Source", lit("Grading"))
df_performance = df_performance.withColumn("Source", lit("Performance"))
df_career = df_career.withColumn("Source", lit("Career"))

# حفظ الداتا كلها في PostgreSQL (من غير ما نختار كولومنات معينة)
df_grading.write \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://postgres:5432/student_db") \
    .option("dbtable", "grading_data") \
    .option("user", "user") \
    .option("password", "password") \
    .option("driver", "org.postgresql.Driver") \
    .mode("overwrite") \
    .save()

df_performance.write \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://postgres:5432/student_db") \
    .option("dbtable", "performance_data") \
    .option("user", "user") \
    .option("password", "password") \
    .option("driver", "org.postgresql.Driver") \
    .mode("overwrite") \
    .save()

df_career.write \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://postgres:5432/student_db") \
    .option("dbtable", "career_data") \
    .option("user", "user") \
    .option("password", "password") \
    .option("driver", "org.postgresql.Driver") \
    .mode("overwrite") \
    .save()

# باقي الكود (حساب الـ department_scores)
# اتحاد الداتا من الجداول الثلاثة
df_combined = df_grading.select("Department", "Total_Score").withColumnRenamed("Total_Score", "Success_Rate") \
    .union(df_performance.select("Department", "Final_Grade").withColumnRenamed("Final_Grade", "Success_Rate")) \
    .union(df_career.select("Field_of_Study", "Career_Satisfaction").withColumnRenamed("Field_of_Study", "Department").withColumnRenamed("Career_Satisfaction", "Success_Rate"))

# حساب المتوسط لكل قسم
df_department_scores = df_combined.groupBy("Department").avg("Success_Rate").withColumnRenamed("avg(Success_Rate)", "Avg_Success_Rate")

# حفظ الـ department_scores في PostgreSQL
df_department_scores.write \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://postgres:5432/student_db") \
    .option("dbtable", "department_scores") \
    .option("user", "user") \
    .option("password", "password") \
    .option("driver", "org.postgresql.Driver") \
    .mode("overwrite") \
    .save()

# إظهار النتيجة
df_department_scores.show()

# إغلاق Spark Session
spark.stop()