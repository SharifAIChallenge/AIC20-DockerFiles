FROM ubuntu:16.04

# Install unzip
RUN apt-get update && apt-get -y install software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update
RUN apt-get install -y sudo openjdk-8-jre-headless python3.5 unzip
RUN apt-get install -y python3-pip
RUN pip3 install numpy

# Copy starter
COPY starter.sh /game/starter.sh
COPY '#FixClient.py' '/game/client/src/#FixClient.py'
ADD libs /libs

# Add runner user
RUN groupadd -r runner --gid=2016 && useradd -M -s /bin/bash -R / runner -u 2016 -g runner

WORKDIR /game
# Run starter
CMD /bin/bash starter.sh
