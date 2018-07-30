FROM python:3.6.5-slim

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY app.py /app/app.py
RUN chmod +x app.py

ENTRYPOINT [ "python","app.py" ]

LABEL maintainer="Nick Kou <nickkounz@gmail.com>" \
    version="1.0"