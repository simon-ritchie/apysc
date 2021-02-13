# How to Develop

## Docker Manipulations

### Build Docker Image

```
$ cd <your project root directory path>
$ docker image build -t action_py_script:0.1.1 .
```

### Create Docker Container

```
$ docker run -it --name action_py_script -v <your host workspace dir>:/mnt/action-py-script -t action_py_script:0.1.1 bash
```

e.g.,

```
$ docker run -it --name action_py_script -v /d/workspace/github/action-py-script:/mnt/action-py-script -t action_py_script:0.1.1 bash
```

### Start Stopping Docker Container

```
docker start action_py_script
docker container exec -it action_py_script bash

```

### Remove Docker Container

```
docker container stop action_py_script
docker container rm action_py_script

```

## Testing

### Run Overall Tests

```
$ pytest --cov=./apyscript tests/ -v -s --workers auto --lf
```

If you want to check coverage missed statement, add `--cov-report term-missing` option:

```
$ pytest --cov=./apyscript tests/ -v -s --workers auto --lf --cov-report term-missing
```

## Apply Lints

### autoflake

```
$ autoflake --in-place --remove-unused-variables --remove-all-unused-imports -r .
```

### isort

```
$ isort --force-single-line-imports .
```

### autopep8

```
$ autopep8 --in-place --aggressive --aggressive -r --ignore=E402 .
```

### flake8

```
$ flake8 --ignore E402,W503 ./
```

### numdoclint

```
$ numdoclint -p ./ -r
```

### mypy

```
$ mypy --ignore-missing-imports --follow-imports skip --disallow-untyped-calls --disallow-untyped-defs --strict-optional --strict-equality ./
```

## PyPI

Build project for PyPI:

```
$ python build.py
```
