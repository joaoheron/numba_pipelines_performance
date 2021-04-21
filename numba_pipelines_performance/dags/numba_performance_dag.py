from datetime import timedelta

from airflow.models import DAG
from airflow.utils import timezone
from airflow.operators.python_operator import PythonOperator

from utils.vars import email_list
from utils.numba_pipelines_performance import (
    calc_elapsed_time_numpy_jit_c,
    calc_elapsed_time_numpy_jit_python,
    calc_elapsed_time_loop_jit_c,
    calc_elapsed_time_loop_jit_python
)


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
    dag_id='numba_performance',
    default_args=default_args,
    schedule_interval=timedelta(minutes=1440),
    dagrun_timeout=timedelta(minutes=45),
)

"""
    Executes python script with numba framework
"""

def build_numba_loop_python(dag):

    return PythonOperator(
        task_id='numba_performance_loop_python',
        python_callable=calc_elapsed_time_loop_jit_python,
        dag=dag
    )

def build_numba_loop_c(dag):

    return PythonOperator(
        task_id='numba_performance_loop_c',
        python_callable=calc_elapsed_time_loop_jit_c,
        dag=dag
    )

def build_numba_numpy_python(dag):

    return PythonOperator(
        task_id='numba_performance_numpy_python',
        python_callable=calc_elapsed_time_numpy_jit_python,
        dag=dag
    )

def build_numba_numpy_c(dag):

    return PythonOperator(
        task_id='numba_performance_numpy_c',
        python_callable=calc_elapsed_time_numpy_jit_c,
        dag=dag
    )

numba_numpy_python = build_numba_numpy_python(dag)
numba_numpy_c = build_numba_numpy_c(dag)

numba_loop_python = build_numba_loop_python(dag)
numba_loop_c = build_numba_loop_c(dag)

numba_loop_python >> numba_numpy_python
numba_loop_c >> numba_numpy_c
