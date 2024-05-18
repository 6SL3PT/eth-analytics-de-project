import joblib
import logging
import psycopg2
import tensorflow as tf

from datetime import date

def run_model_predict() -> None:
    try:
        # Connect to PostgreSQL
        logging.info('Connecting to database...')
        conn = psycopg2.connect(dbname='postgres', user='postgres', 
                                password='postgres', host='postgres')
        curr = conn.cursor()

        # Load input scaler
        logging.info('Loading input scaler...')
        input_scaler = joblib.load(
            '/opt/airflow/dags/python_callable/model/scaler/input_scaler.pkl')

        # Fetch model input data
        SELECT = (
            '''
            SELECT volume_usd,
                tx_count,
                senkou_span_sub,
                alligator_sub
            FROM ethereum.model_input
            WHERE block_timestamp::date = '2024-02-22'
            LIMIT 1
            '''
        )
        logging.info(f'Fetching data for {date.today()} prediction...')
        curr.execute(SELECT)
        model_input = input_scaler.transform(curr.fetchall())

        # Load model
        logging.info('Loading predictive model...')
        model = tf.keras.models.load_model(
            '/opt/airflow/dags/python_callable/model/keras_model/predictive_model.keras')
        
        # Predict
        logging.info(f'Predicting ISI Index of date \'{date.today()}\'...')
        result = model.predict(model_input).squeeze()

        # Insert prediction result
        INSERT = (
            f'''
            INSERT INTO ethereum.model_prediction
                SELECT current_date::timestamptz,
                {result[0]};
            '''
        )
        logging.info(f'Inserting prediction result into model_prediction...')
        curr.execute(INSERT)
        logging.info(f'Insert successfully')

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
