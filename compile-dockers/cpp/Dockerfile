FROM ubuntu:14.04

RUN apt-get update && apt-get install -y \
	build-essential \
	make \
	software-properties-common \
	python-software-properties

RUN add-apt-repository ppa:fkrull/deadsnakes
RUN apt-get update && apt-get install -y \
	python3.5

RUN groupadd -r compiler --gid=2016 && useradd -M -s /bin/bash -R / compiler -u 2016 -g compiler

COPY compile_code /compile_code
COPY utils /utils

CMD python3.5 compile_code/compile.py
