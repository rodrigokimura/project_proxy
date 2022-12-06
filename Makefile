export PIPENV_VERBOSITY=-1
export PYTHONPATH=./src

run:
	@pipenv run python ./src/server.py --hostname ::

lint:
	@pipenv run isort .
	@pipenv run black .
