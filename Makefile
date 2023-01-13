export PIPENV_VERBOSITY=-1
export PYTHONPATH=./src

install:
	@pipenv install --skip-lock

run:
	@pipenv run python ./src/server.py --hostname ::

lint:
	@pipenv run isort .
	@pipenv run black .
