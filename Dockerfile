FROM python:3.6-slim

RUN pip install pytest 

WORKDIR ./src

CMD ["python3","nginx-minder.py"]

