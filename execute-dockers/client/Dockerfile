FROM ubuntu:16.04

# Install unzip
RUN apt-get update && apt-get install software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update
RUN apt-get install -y sudo openjdk-8-jre-headless python3.7 unzip

# Copy starter
COPY starter.sh /game/starter.sh
COPY '#FixClient.py' '/game/client/src/#FixClient.py'
ADD libs /libs

# Add runner user
RUN groupadd -r runner --gid=2016 && useradd -M -s /bin/bash -R / runner -u 2016 -g runner

# Run starter
CMD cd game && /bin/bash starter.sh
