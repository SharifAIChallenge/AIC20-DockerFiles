FROM ubuntu:18.04

RUN apt-get update && apt-get install -y \
	build-essential \
	make \
	software-properties-common \
	cmake \
    wget \
    libssl-dev



RUN cd /usr/local/src \ 
    && wget https://github.com/Kitware/CMake/releases/download/v3.16.4/cmake-3.16.4.tar.gz \
    && tar xvf cmake-3.16.4.tar.gz \ 
    && cd cmake-3.16.4 \
    && ./bootstrap \
    && make \
    && make install \
    && cd .. \
    && rm -rf cmake*

RUN groupadd -r compiler --gid=2016 && useradd -M -s /bin/bash -R / compiler -u 2016 -g compiler

COPY compile_code /compile_code
COPY utils /utils

CMD python3 compile_code/compile.py
