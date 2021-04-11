source ../.env
./run_airflow_command.sh "$1" "airflow" "connections" "-d" "--conn_id" $AIRFLOW_AWS_CONN
./run_airflow_command.sh "$1" "airflow" "connections" "-a" \
    "--conn_id" $AIRFLOW_AWS_CONN \
    "--conn_type" "aws" \
    "--conn_login" $AWS_ACCESS_KEY_ID \
    "--conn_password" $AWS_SECRET_ACCESS_KEY \
    "--conn_extra" "{\"region_name\":\"$AWS_REGION\"}"

./run_airflow_command.sh "$1" "airflow" "connections" "-d" "--conn_id" $POSTGRES_CONNECTION
./run_airflow_command.sh "$1" "airflow" "connections" "-a" \
    "--conn_id" $POSTGRES_CONNECTION \
    "--conn_type" "Postgres" \
    "--conn_host" $DB_HOST \
    "--conn_login" $DB_USER \
    "--conn_password" $DB_PASSWORD \
    "--conn_port" $DB_PORT
