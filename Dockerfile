FROM python:3.6-slim

RUN pip install pytest docopt

COPY ./src/nginx-minder.py /usr/bin/

#WORKDIR ./src

CMD ["nginx-minder.py"]

