from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, lit

# إعداد Spark مع إعدادات MinIO
spark = SparkSession.builder \
    .appName("StudentDataProcessing") \
    .config("spark.hadoop.fs.s3a.endpoint", "http://minio:9000") \
    .config("spark.hadoop.fs.s3a.access.key", "admin") \
    .config("spark.hadoop.fs.s3a.secret.key", "password") \
    .config("spark.hadoop.fs.s3a.path.style.access", "true") \
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
    .getOrCreate()

# قراءة الملفات من MinIO
df1 = spark.read.csv("s3a://student-data/Students_Grading_Dataset.csv", header=True, inferSchema=True)
df2 = spark.read.csv("s3a://student-data/student_performance_large_dataset.csv", header=True, inferSchema=True)
df3 = spark.read.csv("s3a://student-data/education_career_success.csv", header=True, inferSchema=True)

# إضافة عمود "Source" لمعرفة مصدر كل ملف
df1 = df1.withColumn("Source", lit("Grading"))
df2 = df2.withColumn("Source", lit("Performance"))
df3 = df3.withColumn("Source", lit("Career"))

# تعريف الهيكل المشترك (عدلي الأعمدة حسب ملفاتك)
from pyspark.sql.types import StructField, StructType, StringType, DoubleType

common_schema = StructType([
    StructField("Student_ID", StringType(), True),
    StructField("Department", StringType(), True),
    StructField("Total_Score", DoubleType(), True),
    StructField("Attendance (%)", DoubleType(), True),
    StructField("Success_Rate", DoubleType(), True),
    StructField("Source", StringType(), True)
])

# تحويل الأطر إلى الهيكل المشترك (بدون ملء القيم المفقودة بـ NULL مباشرة)
df1_adjusted = df1.select([col(c).cast(common_schema[c].dataType) if c in df1.columns else lit(None).cast(common_schema[c].dataType).alias(c) for c in common_schema.fieldNames()])
df2_adjusted = df2.select([col(c).cast(common_schema[c].dataType) if c in df2.columns else lit(None).cast(common_schema[c].dataType).alias(c) for c in common_schema.fieldNames()])
df3_adjusted = df3.select([col(c).cast(common_schema[c].dataType) if c in df3.columns else lit(None).cast(common_schema[c].dataType).alias(c) for c in common_schema.fieldNames()])

# ملء القيم المفقودة بالمتوسط لكل إطار على حدة
# df1
if "Total_Score" in df1_adjusted.columns:
    avg_total_score_df1 = df1_adjusted.select(avg("Total_Score")).collect()[0][0] or 0
    df1_adjusted = df1_adjusted.fillna({"Total_Score": avg_total_score_df1})
if "Attendance (%)" in df1_adjusted.columns:
    avg_attendance_df1 = df1_adjusted.select(avg("Attendance (%)")).collect()[0][0] or 0
    df1_adjusted = df1_adjusted.fillna({"Attendance (%)": avg_attendance_df1})
if "Success_Rate" in df1_adjusted.columns:
    avg_success_df1 = df1_adjusted.select(avg("Success_Rate")).collect()[0][0] or 0
    df1_adjusted = df1_adjusted.fillna({"Success_Rate": avg_success_df1})

# df2
if "Total_Score" in df2_adjusted.columns:
    avg_total_score_df2 = df2_adjusted.select(avg("Total_Score")).collect()[0][0] or 0
    df2_adjusted = df2_adjusted.fillna({"Total_Score": avg_total_score_df2})
if "Attendance (%)" in df2_adjusted.columns:
    avg_attendance_df2 = df2_adjusted.select(avg("Attendance (%)")).collect()[0][0] or 0
    df2_adjusted = df2_adjusted.fillna({"Attendance (%)": avg_attendance_df2})
if "Success_Rate" in df2_adjusted.columns:
    avg_success_df2 = df2_adjusted.select(avg("Success_Rate")).collect()[0][0] or 0
    df2_adjusted = df2_adjusted.fillna({"Success_Rate": avg_success_df2})

# df3
if "Total_Score" in df3_adjusted.columns:
    avg_total_score_df3 = df3_adjusted.select(avg("Total_Score")).collect()[0][0] or 0
    df3_adjusted = df3_adjusted.fillna({"Total_Score": avg_total_score_df3})
if "Attendance (%)" in df3_adjusted.columns:
    avg_attendance_df3 = df3_adjusted.select(avg("Attendance (%)")).collect()[0][0] or 0
    df3_adjusted = df3_adjusted.fillna({"Attendance (%)": avg_attendance_df3})
if "Success_Rate" in df3_adjusted.columns:
    avg_success_df3 = df3_adjusted.select(avg("Success_Rate")).collect()[0][0] or 0
    df3_adjusted = df3_adjusted.fillna({"Success_Rate": avg_success_df3})

# دمج البيانات بـ union في جدول منفصل (اختياري للتحليل)
merged_df = df1_adjusted.union(df2_adjusted).union(df3_adjusted)

# حفظ الأطر المنفصلة في PostgreSQL
df1_adjusted.write \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://postgres:5432/student_db") \
    .option("dbtable", "grading_data") \
    .option("user", "user") \
    .option("password", "password") \
    .option("driver", "org.postgresql.Driver") \
    .mode("overwrite") \
    .save()

df2_adjusted.write \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://postgres:5432/student_db") \
    .option("dbtable", "performance_data") \
    .option("user", "user") \
    .option("password", "password") \
    .option("driver", "org.postgresql.Driver") \
    .mode("overwrite") \
    .save()

df3_adjusted.write \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://postgres:5432/student_db") \
    .option("dbtable", "career_data") \
    .option("user", "user") \
    .option("password", "password") \
    .option("driver", "org.postgresql.Driver") \
    .mode("overwrite") \
    .save()

# تحليل: حساب متوسط الدرجات حسب القسم (Department) من الجدول المدمج
result = merged_df.groupBy("Department").agg(avg("Total_Score").alias("Avg_Total_Score"))

# حفظ النتائج في PostgreSQL
result.write \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://postgres:5432/student_db") \
    .option("dbtable", "department_scores") \
    .option("user", "user") \
    .option("password", "password") \
    .option("driver", "org.postgresql.Driver") \
    .mode("overwrite") \
    .save()

# عرض النتائج في الـ console (اختبار)
result.show()

# إيقاف Spark
spark.stop()