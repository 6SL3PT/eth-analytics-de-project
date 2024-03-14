FROM apache/airflow:2.8.1


USER root

ARG AIRFLOW_HOME=/opt/airflow

COPY requirements.txt /opt/airflow/


USER airflow

RUN pip install --no-cache-dir apache-airflow==${AIRFLOW_VERSION} -r /opt/airflow/requirements.txt

ENTRYPOINT [ "/opt/airflow/scripts/entrypoint.sh" ]
