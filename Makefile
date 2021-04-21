.PHONY: clean clean-test clean-pyc clean-build docs help
.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os, webbrowser, sys

from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

export SHELL:=/bin/bash
export SHELLOPTS:=$(if $(SHELLOPTS),$(SHELLOPTS):)pipefail:errexit

.ONESHELL:

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

lint: ## check style with flake8
	flake8 airflow/ tests/ docs/

test: ## run tests quickly with the default Python
	pytest

test-all: ## run tests on every Python version with tox
	tox

coverage: ## check code coverage quickly with the default Python
	coverage run --source numba_pipelines_performance -m pytest
	coverage report -m
	coverage html
	$(BROWSER) htmlcov/index.html

docs: ## generate Sphinx HTML documentation, including API docs
	rm -f docs/numba_pipelines_performance.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ numba_pipelines_performance
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	$(BROWSER) docs/_build/html/index.html

servedocs: docs ## compile the docs watching for changes
	watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .

release: dist ## package and upload a release
	twine upload dist/*

dist: clean ## builds source and wheel package
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist

install: clean ## install the package to the active Python's site-packages
	python setup.py install

build:  ## builds project's docker image
	test -n "Airflow Image Version: $(AIRFLOW_IMAGE)"
	read -s -p "Are you sure to build new docker airflow image? (CTRL C FOR CANCELING) "
	echo "==========================================================="
	docker build -t $(AIRFLOW_IMAGE) .

run_locally: build ## builds project's docker image and run it
	function tearDown {
		rm .airflow_vars
		rm .airflow_pools
	}
	trap tearDown EXIT
	read -s -p "Are you sure to run airflow image locally? (CTRL C FOR CANCELING) "
	echo "==========================================================="
	docker rm -f airflow-local || true
	docker run --name airflow-local -d  \
		-e AIRFLOW__CORE__SQL_ALCHEMY_CONN="sqlite:////airflowdb/airflow.db" \
		-e AIRFLOW__CORE__FERNET_KEY=${AIRFLOW__CORE__FERNET_KEY} \
		-p 8088:8080 \
		-v ${PWD}/airflow/dags:/usr/local/airflow/dags \
		-v ${PWD}/airflow/:/tmp/ \
		-v airflow_local_db:/tmp/airflow/ $(AIRFLOW_IMAGE)

	sleep 15
	cd airflow/
	bash airflow_connections.sh local
	envsubst < airflow_vars.json > .airflow_vars
	envsubst < airflow_pools.json > .airflow_pools
	bash run_airflow_command.sh local airflow variables -i /tmp/.airflow_vars
	bash run_airflow_command.sh local airflow pool -i /tmp/.airflow_pools
