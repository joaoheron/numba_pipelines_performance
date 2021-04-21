from datetime import timedelta
from airflow.models import DAG
from airflow.utils import timezone
from airflow.operators.postgres_operator import PostgresOperator
from utils.vars import email_list, DB_NAME, POSTGRES_CONNECTION

start_date = timezone.utcnow().replace(
    minute=0,
    second=0,
    microsecond=0
) - timedelta(hours=1)

default_args = {
    'email': email_list,
    'email_on_failure': True,
    'email_on_retry': False,
    'owner': 'airflow',
    'start_date': start_date,
    'concurrency': 1,
    'retries': 1
}

dag = DAG(
    dag_id='connections_test',
    default_args=default_args,
    schedule_interval=timedelta(minutes=30),
    dagrun_timeout=timedelta(minutes=45),
)

"""
    Checks each half hour if there is still available connection
"""

def build_test_connection_postgres_task(dag):

    select_public = """
        select * from public.orders limit 1;
    """

    return PostgresOperator(
        task_id=f'test_connection_postgres_{DB_NAME}',
        sql=[
            select_public
        ],
        postgres_conn_id=POSTGRES_CONNECTION,
        database=DB_NAME,
        dag=dag
    )

test_postgres_connection_task = build_test_connection_postgres_task(dag)
