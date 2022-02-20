#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."
    export a=$(netstat -tulpen | grep $SQL_PORT)
    while ! [ -z $a ]; do
      sleep 0.1
      export a=$(netstat -tulpen | grep $SQL_PORT)
    done

    echo "PostgreSQL started"
fi

#python manage.py flush --no-input
#python manage.py migrate

exec "$@"
