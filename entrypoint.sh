#!/bin/sh
set -e

python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

# Create a superuser if it doesn't exist
if [ -z "$(python3 manage.py shell -c "from django.contrib.auth.models import User; print(User.objects.filter(username='admin').exists())")" ]; then
    echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@gmail.com', '1')" | python3 manage.py shell
fi

exec "$@"