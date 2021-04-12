FROM puckel/docker-airflow

USER root

RUN usermod -aG root airflow
RUN mkdir /airflowdb/ && chmod -R 770 /airflowdb/

RUN apt-get update \
    && apt-get install -y --no-install-recommends git \
    && apt-get install -y --no-install-recommends vim

USER airflow

COPY requirements.txt /usr/local/airflow/

RUN pip install -U pip

RUN pip install -r /usr/local/airflow/requirements.txt

COPY airflow/dags/ /usr/local/airflow/dags/
