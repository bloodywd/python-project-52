# Makefile
MANAGE := poetry run python3 manage.py

install:
	poetry install

start:
	@$(MANAGE) runserver 0.0.0.0:8000

lint:
	@poetry run flake8 task_manager

migrate:
	@$(MANAGE) makemigrations
	@$(MANAGE) migrate

shell:
	@$(MANAGE) shell_plus

build:
	poetry install
	@$(MANAGE) makemigrations
	@$(MANAGE) migrate