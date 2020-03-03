FROM python:3.7

COPY utils/requirements.txt /utils/requirements.txt
RUN pip3 install -r /utils/requirements.txt
RUN apt-get update && apt-get install -y libsm6 libxext6 libxrender-dev

RUN groupadd -r compiler --gid=2016 && useradd -M -s /bin/bash -R / compiler -u 2016 -g compiler

COPY compile_code /compile_code
COPY utils /utils

CMD python3.7 compile_code/compile.py
