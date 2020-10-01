FROM alpine:3.10

MAINTAINER Mike Ivanov mikonoid@gmail.com

COPY . /app

WORKDIR /app

RUN apk add --update --no-cache \
    python \
    python-dev \
    py-pip \
    build-base \
  && pip install virtualenv \
  && rm -rf /var/cache/apk/*

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "application.py" ]
