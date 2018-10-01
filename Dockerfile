FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1

RUN mkdir /sourcecode
WORKDIR /sourcecode
COPY . /sourcecode/

RUN apk update \
    && apk add vim \
    && apk add build-base gcc abuild binutils binutils-doc gcc-doc zlib-dev \
    && apk add jpeg-dev
RUN pip install -U pip && pip install -r requirements.txt