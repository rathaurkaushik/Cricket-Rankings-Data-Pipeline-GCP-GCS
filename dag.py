# import all module
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2026,9,1),
    'depends_on_past': False,
    'email': ['gcp.labs.practise.7@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# define the DAG
with DAG(
    "cricket_stats_dag",
    default_args=default_args,
    description= "Runs an external Python script",
    schedule_interval='@daily',
    catchup=False,
) as dag:

    # define the tasks
    run_python_script = BashOperator(
        task_id='run_python_script',
        bash_command='python3 /home/airflow/gcs/dags/scripts/extract_pushToGCS.py',
    )

    # set the task dependencies
    run_python_script