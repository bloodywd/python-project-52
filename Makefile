# Makefile
MANAGE := poetry run python3 manage.py

install:
	poetry install

dev:
	@$(MANAGE) runserver

lint:
	@poetry run flake8 task_manager

migrate:
	@$(MANAGE) makemigrations
	@$(MANAGE) migrate

test:
	@$(MANAGE) test

shell:
	@$(MANAGE) shell_plus

start:
	poetry run gunicorn -w 4 task_manager.wsgi

build: install migrate