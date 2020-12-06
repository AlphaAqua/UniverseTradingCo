FROM alpine:3.7
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
#RUN python3 -m ensurepip
#RUN pip3 install --no-cache --upgrade pip setuptools
ADD ./universe.py .
ENTRYPOINT ["python3 universe.py"]
