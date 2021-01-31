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
$ pytest --cov=./apyscript tests/ -v -s --workers auto
```
