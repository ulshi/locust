#!/usr/bin/env sh
date
if [ -z "${TARGET_TASK}" ]; then
  echo "TARGET_TASK not configured" >&2
  exit 1
else
  echo "TARGET_TASK set properly" >&2
fi
date
LOCUST_MODE="${LOCUST_MODE:=standalone}"
_LOCUST_OPTS="-f ${LOCUSTFILE_PATH:-/locustfile.py} ${TARGET_TASK}"
echo ${_LOCUST_OPTS} >&2

if [ "${LOCUST_MODE}" = "master" ]; then
    _LOCUST_OPTS="${_LOCUST_OPTS} --master"
    date
    echo "Mode note 1/3 : Starting Locust in ${LOCUST_MODE} mode..."
    
elif [ "${LOCUST_MODE}" = "slave" ]; then
    if [ -z "${LOCUST_MASTER_HOST}" ]; then
        date
        echo "ERROR: MASTER_HOST is empty. Slave mode requires a master" >&2
        exit 1
    fi
    date
    echo "Mode note 2/3 : Starting Locust in ${LOCUST_MODE} mode..."
    _LOCUST_OPTS="${_LOCUST_OPTS} --slave --master-host=${LOCUST_MASTER_HOST} --master-port=${LOCUST_MASTER_PORT:-5557}"
fi

date
echo "Mode note 3/3 : Starting Locust in ${LOCUST_MODE} mode..."
echo "$ locust ${LOCUST_OPTS} ${_LOCUST_OPTS}"

exec locust ${LOCUST_OPTS} ${_LOCUST_OPTS}
