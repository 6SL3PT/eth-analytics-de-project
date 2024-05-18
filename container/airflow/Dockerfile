FROM apache/airflow:2.8.1-python3.11


USER airflow

COPY requirements.txt /opt/airflow/

RUN pip install --no-cache-dir apache-airflow==${AIRFLOW_VERSION} -r /opt/airflow/requirements.txt
