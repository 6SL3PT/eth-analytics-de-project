from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from python_callable.bigquery.fetch_data import run_fetch_transaction
from python_callable.model.predict import run_model_predict
from python_callable.postgres.postgres_import import run_postgres_import
from python_callable.postgres.process_model_input import run_process_model_input

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
    'daily_batch_dag',
    default_args=default_args,
    start_date=datetime.now(), #+ timedelta(days=1),
    schedule_interval='0 0 * * *',
    description='''
    - Fetch daily data from BigQuery public dataset
    - Process data from PostgreSQL
    - Import final result to PostgreSQL
    - Load model and predict data 
    '''
) as dag:
    fetch_transaction = PythonOperator(
        task_id='get_bigquery_eth_tx',
        python_callable=run_fetch_transaction,
        dag=dag
    )
    postgres_import = PythonOperator(
        task_id='load_tx_to_postgres',
        python_callable=run_postgres_import,
        dag=dag
    )
    fetch_model_input = PythonOperator(
        task_id='process_model_input_data',
        python_callable=run_process_model_input,
        dag=dag
    )
    load_model_and_predict = PythonOperator(
        task_id='load_model_and_predict',
        python_callable=run_model_predict,
        dag=dag
    )

    fetch_transaction >> postgres_import >> fetch_model_input >> load_model_and_predict