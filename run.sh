#! /bin/bash
set -e

if [ ! -f ./notebooks/data/the-movies-dataset.zip ]; then
    echo "Downloading movies dataset..."
    unzip notebooks/data/the-movies-dataset.zip
fi

docker build -t spark_workshop ./docker
docker run --memory=4g -p 8889:8888 -p 4040:4040 -i --rm -v `pwd`/notebooks:/notebooks -t spark_workshop bash -c 'pyspark --driver-memory 16g'