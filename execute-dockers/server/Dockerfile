FROM openjdk:8-jre

RUN apt update
RUN apt install unzip openjfx -y

# Copy server
COPY starter.sh /game/starter.sh

# Expose UI & clients port
EXPOSE 7000
EXPOSE 7099

WORKDIR /game
# Starter
CMD /bin/bash starter.sh 2>&1 | tee -a /game/debug.log
