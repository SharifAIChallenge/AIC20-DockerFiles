FROM isuper/java-oracle

# Install unzip
COPY unzip.deb /unzip.deb
RUN dpkg -i /unzip.deb

# Copy server
COPY server.jar /game/server.jar
COPY server.conf /game/server.conf
COPY starter.sh /game/starter.sh

# Expose UI & clients port
EXPOSE 7000
EXPOSE 7099

# Starter
CMD cd game && /bin/bash starter.sh
