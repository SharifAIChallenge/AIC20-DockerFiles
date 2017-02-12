FROM isuper/java-oracle

# Copy server & starter
COPY AIC16-Logger.jar /game/logger.jar
COPY starter.sh /game/starter.sh

# Starter
CMD cd game && /bin/bash starter.sh
