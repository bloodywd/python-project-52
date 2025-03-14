### Hexlet tests and linter status:
[![Actions Status](https://github.com/bloodywd/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/bloodywd/python-project-52/actions)
[![Github Actions Status](https://github.com/bloodywd/python-project-52/actions/workflows/pyci.yml/badge.svg)](https://github.com/bloodywd/python-project-52/actions)
[![Test Coverage](https://api.codeclimate.com/v1/badges/a914c5ea30f329902f93/test_coverage)](https://codeclimate.com/github/bloodywd/python-project-52/test_coverage)
## About the project.

Task Manager is a task management system similar to http://www.redmine.org. 
It allows you to set tasks, assign performers and change their statuses. Registration and authentication 
are required to work with the system.

## How to start

```
make install
make migrate
make start
```
To use the app you'll need to provide it with $DATABASE_URL and $SECRET_KEY vars.

## System requirements

- Python 3.10
- PostgreSQL or SQLite Database
