# ----------------------------------------------------------------
# helpers/mongodb-cloud-helper
# ----------------------------------------------------------------
install:
	poetry check
	poetry lock
	poetry update
	poetry install

test:
	poetry run pytest --disable-pytest-warnings

build:
	make install
	make test
	poetry build

linters:
	poetry run pre-commit run --all-files
	poetry run flakeheaven lint

freeze:
	poetry run pip freeze > requirements.txt
	poetry run python -m pip install --upgrade pip

all:
	make build
	make linters
	make freeze
