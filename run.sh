#!/bin/bash
#
# TODO: use docker compose instead of this

here=$(readlink -f $0 || $0 && pwd)

make nginx
make nginx-minder
docker run -d -p 80:80 -v "$here/nginx-logs":/var/log/nginx branning/nginx-to-mind
docker run -d -v "$here/nginx-logs":/var/log/nginx branning/nginx-minder
