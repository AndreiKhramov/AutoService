#!/bin/sh

set -e
echo "Waiting for database..."

python src/manage.py shell -c "
import time
from django.db import connection
from django.db.utils import OperationalError

for i in range(30):
    try:
        connection.ensure_connection()
        print('Database is ready')
        break
    except OperationalError:
        print('Database is not ready, waiting...')
        time.sleep(1)
else:
    raise Exception('Database is not available')
"

python src/manage.py migrate
python src/manage.py get_or_createsuperuser
python src/manage.py runserver 0.0.0.0:8000