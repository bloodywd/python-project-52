# Makefile
MANAGE := poetry run python3 manage.py

install:
	poetry install

start:
	@$(MANAGE) runserver

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