#FROM alpine:3.7
#ENV PYTHONUNBUFFERED=1
#RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
#RUN python3 -m ensurepip
#RUN pip3 install --no-cache --upgrade pip setuptools
#RUN pip install numpy

FROM python:3.8-alpine

RUN apk add --update --no-cache py3-numpy
ENV PYTHONPATH=/usr/lib/python3.8/site-packages

ADD ./universe.py /
ENTRYPOINT ["python3", "/universe.py"]
