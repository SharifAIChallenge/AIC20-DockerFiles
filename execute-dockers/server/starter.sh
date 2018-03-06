export AICClient0Name=$client0_id
export AICClient0Token=$client0_token
export AICClient1Name=$client1_id
export AICClient1Token=$client1_token
TIMELIMIT=660

echo 'unzip'
unzip config.zip -d config/

echo 'running'
timeout $TIMELIMIT java -jar server.jar --config=server.conf > /game/Server.txt 2>&1

echo 'Server terminated'
