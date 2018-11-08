Installation:

Build a virtualenv:

> mkdir venv
> virtualenv -p python3 venv
> source venv/bin/activate

Install packages:
> pip install pip-tools
> pip-sync requirements.txt

Update packages:
> pip-compile requirements.in
> pip-sync requirements.txt