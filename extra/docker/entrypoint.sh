#!/bin/bash
set -o pipefail
if [ "$DB" = "sqlite" ]; then
    echo "Using SQLite this is not designed for production"
    if test -f "/opt/openduty/test_sqlite.db"; then
      echo "Container has already been bootstrapped not running migrations"
    else
      echo "Running migrations"
      cd /opt/openduty && python manage.py migrate && echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@admin.com', 'password')" | python manage.py shell
    fi
elif [ "$DB" = "mysql" ]; then
    echo "Using MySQL, Sleeping for 20 seconds to wait for process to boot"
    sleep 20
    DB_OUTPUT=`echo "SHOW TABLES LIKE 'auth_group';" | mysql -h $DB_HOST -u "$DB_USER" --password="$DB_PASSWORD" $DB_NAME |tail -n 1 2>&1`
    if [[ $DB_OUTPUT == *"auth_group"* ]]; then
       echo "Database bootstrapped"
       echo "Running dbsync"
       python manage.py syncdb
    else
       echo "Copying settings and running migrations"
       mv /opt/openduty/openduty/settings.py.mysql /opt/openduty/openduty/settings.py
       cd /opt/openduty && python manage.py migrate
       python manage.py migrate
       echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@admin.com', 'password')" | python manage.py shell
       python manage.py syncdb
    fi
else
    echo "Unsupported Database $DB"
    exit 100
fi
/usr/bin/supervisord
