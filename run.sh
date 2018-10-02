#! /bin/bash
set -e

docker build -t movie_stats ./docker
docker run --memory=4g -p 8889:8888 -p 4040:4040 -i --rm -v `pwd`/notebooks:/notebooks -t movie_stats bash -c 'pyspark --driver-memory 16g'