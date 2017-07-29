
all: dockerfile

dockerfile:
	docker build . --tag nginx-minder
.phony: all dockerfile

