.phony: envrc install runserver secretkey venv

env:
	echo DJANGO_SECRET_KEY=`python -c "import secrets; print(secrets.token_urlsafe())"` > ~/.virtualenvs/`cat .venv`/.env

install:
	pip install -r requirements.txt

migrate:
	python manage.py migrate

runserver:
	python manage.py runserver

secretkey:
	python -c "import secrets; print(secrets.token_urlsafe())"

venv:
	basename `pwd` > .venv
	rm -rf ~/.virtualenvs/`cat .venv`
	python3 -m venv ~/.virtualenvs/`cat .venv`
	exec fish
