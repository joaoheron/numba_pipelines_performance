ARGS_LIST=${@:2}
echo "airflow command: $ARGS_LIST"

if [ "$1" = "local" ]; then
    echo 'running locally'
    docker exec \
        -e AIRFLOW__CORE__SQL_ALCHEMY_CONN="sqlite:////airflowdb/airflow.db" \
        -e AIRFLOW__CORE__FERNET_KEY="$AIRFLOW__CORE__FERNET_KEY" \
        -it airflow-local \
        $ARGS_LIST
else
    echo 'running prod'
    docker run \
      -v $PWD/:/tmp/ \
      -e AIRFLOW__CORE__SQL_ALCHEMY_CONN="$AIRFLOW__CORE__SQL_ALCHEMY_CONN" \
      -e AIRFLOW__CORE__FERNET_KEY="$AIRFLOW__CORE__FERNET_KEY" \
      -it $AIRFLOW_IMAGE \
      $ARGS_LIST
fi