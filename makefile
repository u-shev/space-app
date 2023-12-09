run:
	poetry run python manage.py runserver 0.0.0.0:8000

install: 
	poetry install

migrate:
	poetry run python3 manage.py makemigrations
	poetry run python3 manage.py migrate

lint:
	poetry run flake8 space_app

start:
	poetry run uvicorn space_app.asgi:application

worker:
	celery -A space_app worker -l info

beat:
	celery -A space_app beat -l info

test:
	poetry run python3 manage.py test

test-coverage:
	poetry run coverage run manage.py test
	poetry run coverage report -m --include=space_app/* --omit=space_app/settings.py
	poetry run coverage xml --include=space_app/* --omit=space_app/settings.py
