# PROJET-FIL-ROUGE
PROJET FIL ROUGE

## create envirenment
python3 -m venv venv
source venv/bin/activate

## run minio
create bucket manuelment named "student-data" in "http://localhost:9000"

python3 minio/upload_to_minio.py

## now spark job 

docker-compose exec spark spark-submit --jars /tmp/spark_jobs/lib/postgresql-42.7.3.jar /spark_jobs/spark_job.py

## check postgesql 
docker-compose exec postgres psql -U user -d student_db
\dt
SELECT * FROM department_scores LIMIT 5;
