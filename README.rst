===========================
Numba Pipelines Performance
===========================


.. image:: https://img.shields.io/pypi/v/numba_pipelines_performance.svg
        :target: https://pypi.python.org/pypi/numba_pipelines_performance

.. image:: https://img.shields.io/travis/joaoheron/numba_pipelines_performance.svg
        :target: https://travis-ci.com/joaoheron/numba_pipelines_performance

.. image:: https://readthedocs.org/projects/numba-pipelines-performance/badge/?version=latest
        :target: https://numba-pipelines-performance.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status




This project uses Numba, an open source JIT compiler that translates Python functions to optimized machine code at runtime, to compare Apache Airflow DAG performances between accelerated and non-accelerated methods.


* Free software: Apache Software License 2.0
* Documentation: https://numba-pipelines-performance.readthedocs.io.


Getting started 

- Check codestyle with flake8:

    $ make lint

- Run tests with the default Pytest library:

    $ make test

- Generate Sphinx HTML documentation, including API docs:

    $ make docs

- Compile the docs watching for changes:

    $ make servedocs

- Builds project's docker image:

    $ make build_project

- Builds project's docker image and run it:

    $ make run_project_locally
