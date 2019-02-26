FROM openjdk:8-jre

RUN apt update
RUN apt install unzip openjfx -y

# Copy server
COPY server.jar /game/server.jar
COPY server.template.conf /game/server.template.conf
COPY starter.sh /game/starter.sh

# Expose UI & clients port
EXPOSE 7000
EXPOSE 7099

# Starter
CMD cd game && /bin/bash starter.sh | tee -a /game/debug.log
