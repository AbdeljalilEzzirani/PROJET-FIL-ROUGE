# from minio import Minio

# client = Minio("localhost:9000", access_key="admin", secret_key="password", secure=False)
# client.fput_object("student-data", "Students_Grading_Dataset.csv", "/home/abdeljalil/Desktop/PROJET_FIL_ROUGE_ALL/PROJET-FIL-ROUGE/data/Students_Grading_Dataset.csv")
# client.fput_object("student-data", "student_performance_large_dataset.csv", "/home/abdeljalil/Desktop/PROJET_FIL_ROUGE_ALL/PROJET-FIL-ROUGE/data/student_performance_large_dataset.csv")
# client.fput_object("student-data", "education_career_success.csv", "/home/abdeljalil/Desktop/PROJET_FIL_ROUGE_ALL/PROJET-FIL-ROUGE/data/education_career_success.csv")

# from minio import Minio

# client = Minio("localhost:9000", access_key="admin", secret_key="password", secure=False)

# client.fput_object(
#     "student-data",
#     "Students_Grading_Dataset.csv",
#     "/home/abdeljalil/Desktop/PROJET_FIL_ROUGE_ALL/PROJET-FIL-ROUGE_Batch/data/Students_Grading_Dataset.csv"
# )
# client.fput_object(
#     "student-data",
#     "student_performance_large_dataset.csv",
#     "/home/abdeljalil/Desktop/PROJET_FIL_ROUGE_ALL/PROJET-FIL-ROUGE_Batch/data/student_performance_large_dataset.csv"
# )
# client.fput_object(
#     "student-data",
#     "education_career_success.csv",
#     "/home/abdeljalil/Desktop/PROJET_FIL_ROUGE_ALL/PROJET-FIL-ROUGE_Batch/data/education_career_success.csv"
# )

# print("Files uploaded successfully to MinIO!")


from minio import Minio
from minio.error import S3Error

client = Minio("localhost:9000", access_key="admin", secret_key="password", secure=False)

# التأكد من وجود الـ bucket وإنشاؤها لو مش موجودة
bucket_name = "student-data"
try:
    if not client.bucket_exists(bucket_name):
        client.make_bucket(bucket_name)
        print(f"Bucket '{bucket_name}' created successfully!")
    else:
        print(f"Bucket '{bucket_name}' already exists!")
except S3Error as err:
    print(f"Error: {err}")
    exit(1)

# رفع الملفات
client.fput_object(
    bucket_name,
    "Students_Grading_Dataset.csv",
    "/home/abdeljalil/Desktop/PROJET_FIL_ROUGE_ALL/PROJET-FIL-ROUGE_Batch/data/Students_Grading_Dataset.csv"
)
client.fput_object(
    bucket_name,
    "student_performance_large_dataset.csv",
    "/home/abdeljalil/Desktop/PROJET_FIL_ROUGE_ALL/PROJET-FIL-ROUGE_Batch/data/student_performance_large_dataset.csv"
)
client.fput_object(
    bucket_name,
    "education_career_success.csv",
    "/home/abdeljalil/Desktop/PROJET_FIL_ROUGE_ALL/PROJET-FIL-ROUGE_Batch/data/education_career_success.csv"
)

print("Files uploaded successfully to MinIO!")