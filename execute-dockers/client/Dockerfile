FROM ubuntu

# Install unzip
COPY unzip.deb /unzip.deb
RUN dpkg -i /unzip.deb
RUN apt-get update
RUN apt-get install -y sudo openjdk-8-jre-headless 

# Copy starter
COPY starter.sh /game/starter.sh
COPY '#FixClient.py' '/game/client/src/#FixClient.py'
ADD libs /libs

# Add runner user
RUN groupadd -r runner --gid=2016 && useradd -M -s /bin/bash -R / runner -u 2016 -g runner

# Run starter
CMD cd game && /bin/bash starter.sh
