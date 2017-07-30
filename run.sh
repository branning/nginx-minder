#!/bin/bash
#
# TODO: use docker compose instead of this

make nginx
make nginx-minder
docker run -d -p 80:80 custom-nginx
docker run -d nginx-minder
