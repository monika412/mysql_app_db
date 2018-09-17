#!/usr/bin/env bash

docker_name='db_docker'
docker_image=$1

if [ ! "$(docker ps -q -f name=$docker_name)" ]; then
    if [ "$(docker ps -aq -f status=exited -f name=$docker_name)" ]; then
        # cleanup
        docker rm $docker_name
    fi
    # run your container
    docker run -d --name $docker_name $docker_image
fi