FROM openjdk:8-jdk

RUN apt update && apt install -y \
	software-properties-common

RUN apt update && apt install -y \
        openjfx

RUN groupadd -r compiler --gid=2016 && useradd -M -s /bin/bash -R / compiler -u 2016 -g compiler

COPY compile_code /compile_code
COPY utils /utils
COPY libs /libs

CMD python3.7 compile_code/compile.py
