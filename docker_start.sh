#!/usr/bin/env sh

if [ -z "${TARGET_TASK}" ]; then
  echo "TARGET_TASK not configured" >&2
  exit 1
else
  echo "TARGET_TASK set properly" >&2
fi

LOCUST_MODE="${LOCUST_MODE:=standalone}"
_LOCUST_OPTS="-f ${LOCUSTFILE_PATH:-/locustfile.py} ${TARGET_TASK}"
echo ${_LOCUST_OPTS} >&2

echo "Mode note 2/3 : Starting Locust in ${LOCUST_MODE} mode..."
_LOCUST_OPTS="${_LOCUST_OPTS} --slave --master-host=${LOCUST_MASTER_HOST} --master-port=${LOCUST_MASTER_PORT:-5557}"

echo "Mode note 3/3 : Starting Locust in ${LOCUST_MODE} mode..."
echo "$ locust ${LOCUST_OPTS} ${_LOCUST_OPTS}"

exec locust ${LOCUST_OPTS} ${_LOCUST_OPTS}
