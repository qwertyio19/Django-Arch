#!/bin/bash

set -euo pipefail

DATE=$(date "+%Y-%m-%d")
BASE_DIR=/opt/services/bsu/bsu_backend
SRC_DIR="$BASE_DIR"
MANAGE_PY="$SRC_DIR/manage.py"
GUNICORN_CONFIG="$BASE_DIR/config/settings/gunicorn_config.py"
LOG_DIR="$BASE_DIR/devops/distributions/backend"
LOG_FILE="$BASE_DIR/devops/distributions/backend/deploy_${DATE}.log"

log() {
    local message="$1"
    echo "$(date "+%Y-%m-%d %H:%M:%S") - $message" >> "$LOG_FILE"
}

check_directories() {
    if [ -z "$(ls -A ${LOG_DIR})" ]; then
        mkdir -p ${LOG_DIR}
    fi
}

check_dependencies() {
    command -v python3 >/dev/null 2>&1 || { echo >&2 "Python3 не установлен. Установите его и повторите попытку."; exit 1; }
    command -v gunicorn >/dev/null 2>&1 || { echo >&2 "Gunicorn не установлен. Установите его и повторите попытку."; exit 1; }
}

cd_to_directory() {
    local dir="$1"
    cd "$dir" || { log "Ошибка: Не удалось перейти в директорию $dir"; exit 1; }
}

run_django_command() {
    local command="$1"
    log "Выполняю команду: $command"
    python3 "$MANAGE_PY" $command || { log "Ошибка: Не удалось выполнить команду $command"; exit 1; }
}

handle_error() {
    local error_message="$1"
    log "Ошибка: $error_message"
    exit 1
}

check_dependencies

check_directories

cd_to_directory "$SRC_DIR"

run_django_command "makemigrations"

run_django_command "migrate"

run_django_command "collectstatic --no-input"

cd_to_directory "$BASE_DIR"

log "$GUNICORN_CONFIG"

# log "Запускаю сервер с помощью Gunicorn..."
# gunicorn config.wsgi --config "$GUNICORN_CONFIG" || handle_error "Не удалось запустить сервер с помощью Gunicorn"

log "Запускаю сервер с помощью Gunicorn и перенаправляю stdout/stderr в $LOG_FILE..."

# &> означает перенаправление stdout и stderr
# '>>' означает добавление в конец файла (append)
# 'exec' гарантирует, что Gunicorn станет PID 1
exec gunicorn config.wsgi --config "$GUNICORN_CONFIG" &>> "$LOG_FILE" || handle_error "Не удалось запустить сервер с помощью Gunicorn"