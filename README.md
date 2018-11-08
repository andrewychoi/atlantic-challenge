# Installation:

## Set up a virtualenv:

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


# Things to fix
Currently using a SQLite DB, which is included in repo. This is bad practice! Migrate to relational DB that's hosted elsewhere--e.g. PostgreSQL

The templates are currently uglier than sin, but the functionality is there!

# Extra credit
From spec:

- [✓] A full git history showing your development style.
	- included in tarball
- [✓] Normalization of the database
	- check out `atlantic/orders/models.py`
- [✓ ish] Authentication and authorization capabilities
	- to protect the upload, we would need to build a few templates. Django gives us auth + auth out of the box:
	- https://docs.djangoproject.com/en/2.1/topics/auth/default/
- [✓ ish] Support for files larger than 3MB (upload progress indicator, etc)
	- As long as we have enough memory!
- [✕] Irregularity detection and alerting (for instance, if a purchase is canceled that has not been previously seen as new)
	- Comments in `atlantic/orders/views.py` address where this logic goes
- [✕] Detecting and handling updating addresses for customers
	- See above
- [✕] Tests
	- Ran out of time--but model logic testing is easy to mock:
	- https://docs.djangoproject.com/en/2.1/topics/testing/overview/


