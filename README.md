# Installation:

## Build a virtualenv:

> mkdir venv
> virtualenv -p python3 venv
> source venv/bin/activate

## Install packages:
> pip install pip-tools
> pip-sync requirements.txt

## Run migrations:
> cd atlantic
> python manage.py migrate

## Start server:
> python manage.py runserver

## Examine:
In browser, go to localhost:8000
For inserted items, check localhost:8000/admin/

# Credentials:
Existing database has a superuser: username:password == andrew:andrew
To create new ones:
> python manage.py createsuperuser

# For maintenance

Update packages:
> pip-compile requirements.in
> pip-sync requirements.txt


Things to fix:
Currently using a SQLite DB, which is included in repo. This is bad practice! Migrate to relational DB that's hosted elsewhere--e.g. PostgreSQL



