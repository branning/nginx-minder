
all: nginx nginx-minder

nginx: ./nginx/nginx.conf ./nginx/Dockerfile
	docker build ./nginx/ --tag nginx-to-mind

nginx-minder:
	docker build . --tag nginx-minder

push:
	docker push branning/nginx-minder
	docker push branning/nginx-to-mind

.PHONY: all nginx nginx-minder

