from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from transactions.fetch_transaction import run_fetch_transaction
from transactions.postgres_import import run_postgres_import


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@test.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retires': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'transactions_dag',
    default_args=default_args,
    start_date=datetime.now() + timedelta(days=1),
    schedule_interval='0 0 * * *',
    description='Fetch daily transactions data from BigQuery public dataset'
) as dag:
    fetch_transaction = PythonOperator(
        task_id='get_bigquery_eth_tx',
        python_callable=run_fetch_transaction,
        dag=dag
    )

    postgres_import = PythonOperator(
        task_id='load_to_postgres',
        python_callable=run_postgres_import,
        dag=dag
    )

    fetch_transaction >> postgres_import