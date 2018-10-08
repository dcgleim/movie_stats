#! /bin/bash
set -e

docker build -t movie_stats ./docker
docker run --memory=4g -p 8889:8888 -i --rm -v `pwd`/notebooks:/notebooks -t movie_stats bash -c 'jupyter notebook --port 8888 --ip=0.0.0.0 --allow-root --config /notebooks/.config.py --no-browser --notebook-dir=/notebooks'