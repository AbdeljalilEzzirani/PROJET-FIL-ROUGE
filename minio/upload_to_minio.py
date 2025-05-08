from minio import Minio

client = Minio("localhost:9000", access_key="admin", secret_key="password", secure=False)  # غير 9001 إلى 9000
client.fput_object("student-data", "Students_Grading_Dataset.csv", "/home/abdeljalil/Desktop/PROJET_FIL_ROUGE/data/Students_Grading_Dataset.csv")
client.fput_object("student-data", "student_performance_large_dataset.csv", "/home/abdeljalil/Desktop/PROJET_FIL_ROUGE/data/student_performance_large_dataset.csv")
client.fput_object("student-data", "education_career_success.csv", "/home/abdeljalil/Desktop/PROJET_FIL_ROUGE/data/education_career_success.csv")