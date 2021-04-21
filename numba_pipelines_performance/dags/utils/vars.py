from airflow.models import Variable

DB_HOST = Variable.get("DB_HOST")
DB_USER = Variable.get("DB_USER")
DB_PASSWORD = Variable.get("DB_PASSWORD")
DB_NAME = Variable.get("DB_NAME")
DB_PORT = Variable.get("DB_PORT")

S3_BUCKET = Variable.get("S3_BUCKET")
S3_KEY = Variable.get("S3_KEY")
POSTGRES_CONNECTION = Variable.get("POSTGRES_CONNECTION")
AIRFLOW_AWS_CONN = Variable.get("AIRFLOW_AWS_CONN")
AWS_ACCESS_KEY_ID = Variable.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = Variable.get("AWS_SECRET_ACCESS_KEY")

email_list = [
    'your@mail.com'
]
