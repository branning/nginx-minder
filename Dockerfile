FROM python:3.6-slim

RUN pip install docopt

COPY ./src/nginx_minder.py /usr/local/bin/

CMD ["nginx_minder.py"]

