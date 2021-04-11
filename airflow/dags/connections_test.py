from datetime import timedelta
from airflow.models import DAG
from utils import common_tasks
from airflow.utils import timezone
from utils.vars import email_list

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
        select * from public.sample_table limit 1;
    """

    return PostgresOperator(
        task_id=f'test_connection_postgres_{POSTGRES_DB_NAME}',
        sql=[
            select_public
        ],
        postgres_conn_id=AIRFLOW_POSTGRES_CONN,
        database=POSTGRES_DB_NAME,
        dag=dag
    )

test_postgres_connection_task = common_tasks.build_test_connection_postgres_task(dag)

