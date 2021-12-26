#!/bin/sh


image=$(basename $PWD)
docker build -t "${image}:latest" .
