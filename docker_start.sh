#!/usr/bin/env sh

if [ -z "${TARGET_TASK}" ]; then
  echo "ERROR: TARGET_TASK not configured" >&2
  exit 1
elif 1; then
  echo "TARGET_TASK set properly" >&2
fi

LOCUST_MODE="${LOCUST_MODE:=standalone}"
_LOCUST_OPTS="-f ${LOCUSTFILE_PATH:-/locustfile.py} ${TARGET_TASK}"
echo ${_LOCUST_OPTS} >&2

if [ "${LOCUST_MODE}" = "master" ]; then
    _LOCUST_OPTS="${_LOCUST_OPTS} --master"
elif [ "${LOCUST_MODE}" = "slave" ]; then
    if [ -z "${LOCUST_MASTER_HOST}" ]; then
        echo "ERROR: MASTER_HOST is empty. Slave mode requires a master" >&2
        exit 1
    fi

    _LOCUST_OPTS="${_LOCUST_OPTS} --slave --master-host=${LOCUST_MASTER_HOST} --master-port=${LOCUST_MASTER_PORT:-5557}"
fi

echo "Starting Locust in ${LOCUST_MODE} mode..."
echo "$ locust ${LOCUST_OPTS} ${_LOCUST_OPTS}"

exec locust ${LOCUST_OPTS} ${_LOCUST_OPTS}
