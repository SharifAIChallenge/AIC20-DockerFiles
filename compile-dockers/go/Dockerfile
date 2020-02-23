FROM golang:1.13.8

RUN apt update && apt install -y \
	software-properties-common

RUN apt update && apt install -y \
        openjfx

RUN groupadd -r compiler --gid=2016 && useradd -M -s /bin/bash -R / compiler -u 2016 -g compiler

WORKDIR /
COPY compile_code /compile_code
COPY utils /utils

CMD python3.7 compile_code/compile.py
