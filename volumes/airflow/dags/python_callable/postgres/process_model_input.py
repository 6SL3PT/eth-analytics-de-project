import logging
import psycopg2

from datetime import date, timedelta


def run_process_model_input() -> None:
    try:
        # Connect to PostgreSQL
        logging.info('Connecting to database...')
        conn = psycopg2.connect(dbname='postgres', user='postgres', 
                                password='postgres', host='postgres')
        curr = conn.cursor()

        # Fetch data and insert to model_input
        with open('/opt/airflow/dags/python_callable/postgres/sql/process_model_input.sql', 'r') as f:
            SQL = f.read()
        logging.info(f'Start insert input of date \'{date.today() - timedelta(days=1)}\' into model_input')

        # Execute insert command
        curr.execute(SQL)
        logging.info(f'INSERT {curr.rowcount}')
        assert curr.rowcount == 1

        # Commit insert
        conn.commit()
        logging.info('Successfully commit insert')

    except (Exception, psycopg2.DatabaseError) as err:
        logging.error('Error in transaction, reverting all changes using rollback ', err)
        conn.rollback()
        raise err

    finally:
        if conn:
            curr.close()
            conn.close()
            logging.info('psycopg2 cursor closed')