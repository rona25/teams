#!/usr/bin/env bash
set -o errexit
set -o pipefail

# input variables
BIND_HOST=${1:-127.0.0.1}
API_PORT=${2:-8080}
ADMIN_PORT=${3:-8081}

# static variables
BASE_DIR=$(cd $(dirname $0)/.. && pwd)
LOG_DIR=${BASE_DIR}/tmp/logs
CONF_DIR=${BASE_DIR}/conf
VENV_DIR=${BASE_DIR}/venv
SUPERVISORD=${BASE_DIR}/venv/bin/supervisord

# check arguments
if [ "-h" = "${BIND_HOST}" ] ; then
    echo "Usage: $0 <HOST> <API PORT> <ADMIN PORT>"
    exit 0
fi

set -o nounset

# ensure the log dir exists
mkdir -p ${LOG_DIR}

# launch server
BIND_HOST=${BIND_HOST} \
    API_PORT=${API_PORT} \
    ADMIN_PORT=${ADMIN_PORT} \
    LOG_DIR=${LOG_DIR} \
    VENV_DIR=${VENV_DIR} \
    ${SUPERVISORD} \
    -c ${CONF_DIR}/supervisord.conf
