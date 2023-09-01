#!/bin/sh

# A script to allow for easy local verification that docker containers are still working

DOCKER_ENVIRONMENT=$1
SHOULD_RUN=$2

# Colours
RED='\033[0;31m'
YELLOW='\033[0;33m'
NC='\033[0m' # No Color

if [ $DOCKER_ENVIRONMENT = "prod" ]
then
    echo "Building the production docker image..."
    docker build --target production --tag todo-app:prod .
    if [ $SHOULD_RUN = "true" ]
    then
        echo "Running the production docker image..."
        docker run --env-file .env -p 127.0.0.1:8000:80/tcp --name tasko-prod -d todo-app:prod || echo "${YELLOW}Make sure you have deleted the currently running prod container...${NC}"
    fi
fi

if [ $DOCKER_ENVIRONMENT = "dev" ]
then
    echo "Building the development docker image..."
    docker build --target development --tag todo-app:dev .
    if [ $SHOULD_RUN = "true" ]
    then
        echo "Running the development docker image..."
        docker stop tasko-dev && docker rm tasko-dev
        # Note we develop against port 8001 so we can have production and development running simultaneously
        docker run --env-file .env -p 127.0.0.1:8001:80/tcp --name tasko-dev -d --mount type=bind,source="$(pwd)"/todo_app,target=/todo_app todo-app:dev
    fi
fi

if [ $DOCKER_ENVIRONMENT = "test" ]
then
    echo "Building the test docker image..."
    docker build --target test --tag todo-app:test .
    if [ $SHOULD_RUN = "true" ]
    then
        echo "Running the test docker image..."
        docker stop tasko-test && docker rm tasko-test
        docker run --name tasko-test todo-app:test
    fi
fi