FROM python:3.7-alpine

RUN apk add --no-cache build-base openssl-dev libffi-dev \
    && pip install pylxd cherrypy json2html \
    && rm -rf ~/.cache
COPY main.py /
EXPOSE 8080

ENTRYPOINT [ "python3", "/main.py"]
