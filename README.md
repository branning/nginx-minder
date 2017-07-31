# nginx-minder
Watch nginx logs and periodically report status code counts in statsd format.

## About

The `nginx-minder` program is distributed with a Dockerfile and configuraiton
files to run it to monitor the logs from a group of Nginx instances deployed in
a high-availability Kubernetes cluster.

## What does it do?

On each nginx instance, the local access log file at `/var/log/nginx/access.log`
is followed, and the HTTP status code of each route accessed on the server is
noted. For any routes that produce status codes in the `500-599` range
(fatal error codes), the route that produced the code is also noted. Every 5
seconds, the total count of `200`, `300`, `400`, `500` status codes is printed
in `statsd`-compatible log messages, followed by a list of routes that produced
`500` status codes with the code count.

## Deployment

The containers are built and stored in [Docker Hub](http://hub.docker.com/branning/nginx-minder).
In order to build the containers, you can run `make`. In order to push new 
containers that will be pulled by the [Kubernetes deployment](k8s/nginx-minder-deployment.yaml), 
you must first login to the Docker Hub repository:

    docker login --username=branning

After logging in, you can push new containers with `make push`.
 

