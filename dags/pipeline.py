from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime
 
with DAG('pipeline', start_date=datetime(2023, 6, 23),
schedule_interval='@daily', catchup=False) as dag:
    task1 = BashOperator(
        task_id = 'Postgre_Extraction',
        bash_command = 'python3 /code/dags/scripts/psql_extract.py'
    )

    task2 = BashOperator(
        task_id='CSV_Extraction',
        bash_command='python3 /code/dags/scripts/csv_extract.py',
    )

    task3 = BashOperator(
        task_id = 'SQLite_Creation',
        bash_command='python3 /code/dags/scripts/sqlite_load.py'
    )

    task4 = BashOperator(
        task_id = 'Final_Query',
        bash_command='python3 /code/dags/scripts/sqlite_query.py'
    )

    task1 >> task2 >> task3 >> task4