FROM alpine:latest

WORKDIR /app

COPY . /app

RUN apk add --update --no-cache \
    python3 \
    py3-pip \
    && pip3 install --upgrade pip \
    && pip3 install virtualenv \
    && rm -rf /var/cache/apk/*

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
#
