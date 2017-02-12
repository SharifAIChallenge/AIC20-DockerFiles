FROM ubuntu

# Install unzip
COPY unzip.deb /unzip.deb
RUN dpkg -i /unzip.deb

# Copy starter
COPY starter.sh /game/starter.sh

# Add runner user
RUN groupadd -r runner --gid=2016 && useradd -M -s /bin/bash -R / runner -u 2016 -g runner

# Run starter
CMD cd game && /bin/bash starter.sh
