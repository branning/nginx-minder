
all: nginx nginx-minder

nginx: ./nginx/nginx.conf ./nginx/Dockerfile
	docker build ./nginx/ --tag custom-nginx

nginx-minder:
	docker build . --tag nginx-minder

.PHONY: all nginx nginx-minder

