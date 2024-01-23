#!/bin/sh
set -e

python3 manage.py makemigrations --noinput
python3 manage.py migrate --fake --noinput

exec "$@"