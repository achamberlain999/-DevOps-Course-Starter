
## Docker

### Building and running the images for local verification

The `Dockerfile` contains all the configuration for the images.

Instructions to build and run the docker images are documented in code in `tools/docker_build.sh`. To build (and optionally run) containers, you can use the following command:

```sh tools/docker_build.sh <environment> <should_run>```

where `environment` is one of dev/test/prod, and `should_run` can be set as true to run the newly built container.

**Warning!** This should not be used for building a production container to deploy!

#### Parameter meanings

1. `env-file` tells the container where to fetch the environment variables from
1. `-p IP:HOST_PORT:DOCKER_PORT/protocol` matches up an IP and port on your local machine to a PORT in the container
1. `--name` specifies a name for the container so it can be easily referred to in future
1. `-d` prevents the container from being attached to your current terminal
1. `--mount` creates a bind mount meaning that the docker container will treat its local `/todo_app` directory as the `$(pwd)"/todo_app` directory in your filesystem, 
allowing you to develop the app inside a docker container with hot reloading.

### Building the production docker image locally

Use the following command to build the production docker image. Warning: if you are working on an M1 Mac you must specify the platform as shown below. Docker will build an image for the architecture of your machine, but the container will fail to start up in Azure if you push an M1 image.

```docker build --platform linux/amd64 --target production --tag alechasoftwire/todo-app:prod .```

### Pushing the production docker image to Docker Hub

Requires credentials for the docker hub account:

```shell
docker login
docker push alechasoftwire/todo-app:prod
```