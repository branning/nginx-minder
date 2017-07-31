FROM branning/nginx-minder

RUN pip install pytest

COPY ./test/test_nginx_minder.py /test

WORKDIR /test

CMD ["py.test"]

