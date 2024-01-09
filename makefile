run:
	poetry run python ./space_app/manage.py runserver 0.0.0.0:8000

install: 
	poetry install

migrate:
	poetry run python3 ./space_app/manage.py makemigrations
	poetry run python3 ./space_app/manage.py migrate

lint:
	poetry run flake8 space_app

start:
	poetry run gunicorn -w 5 -b 0.0.0.0:8000 space_app.wsgi

worker:
	celery -A space_app worker -l info

beat:
	celery -A space_app beat -l info

test:
	poetry run python3 ./space_app/manage.py test posts users

test-coverage:
	poetry run coverage run ./space_app/manage.py test posts users
	poetry run coverage report -m --include=space_app/* --omit=space_app/settings.py
	poetry run coverage xml --include=space_app/* --omit=space_app/settings.py
