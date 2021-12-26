#!/bin/sh


#UID=$(id -u)
#GID=$(id -g)
image=$(basename $PWD)

docker run  -d  --network host --volume  $PWD/data:/data  -it   "${image}:latest"

#Run your Docker Image
