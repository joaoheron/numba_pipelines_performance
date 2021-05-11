# Numba Pipelines Performance

This project uses Numba, an open source JIT compiler that translates Python functions to optimized machine code at runtime, to compare Apache Airflow DAG performances between accelerated and non-accelerated methods.


* Free software: Apache Software License 2.0
* Documentation: https://numba-pipelines-performance.readthedocs.io.


### Getting started
--------

- Display all make cli commands options and descriptions:
```bash
    make help
```

- Remove all build, test, coverage and Python artifacts:
```bash
    make clean
```

- Check codestyle with flake8:
```bash
    make lint
```

- Run tests with the default Pytest library:
```bash
    make test
```

- Check code coverage quickly with the default Python:
```bash
    make coverage
```

- Generate Sphinx HTML documentation, including API docs:
```bash
    make docs
```

- Compile the docs watching for changes:
```bash
    make servedocs
```

- Builds project's docker image
```bash
    make build_project
```

- Builds project's docker image and run it locally
```bash
    make run_project_locally
```
