#! /bin/sh
set -e

docker build -t movie_stats ./docker

docker run --rm \
  --memory=4g \
  -p 8889:8888 -p 4040:4040 \
  -v "$(pwd)/notebooks:/notebooks" \
  movie_stats