
all: nginx nginx-minder

nginx: ./nginx/nginx.conf ./nginx/Dockerfile
	docker build ./nginx/ --tag branning/nginx-to-mind

nginx-minder:
	docker build . --tag branning/nginx-minder

nginx-minder-test: nginx-minder
	docker build ./test/ --tag nginx-minder-test

test: nginx-minder-test
	docker run nginx-minder-test

push:
	docker push branning/nginx-minder
	docker push branning/nginx-to-mind

.PHONY: all nginx nginx-minder

