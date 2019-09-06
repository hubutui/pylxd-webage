FROM python:3.7-slim

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pylxd cherrypy json2html \
    && rm -rf ~/.cache
COPY main.py /
EXPOSE 8080

ENTRYPOINT [ "python3", "/main.py"]
