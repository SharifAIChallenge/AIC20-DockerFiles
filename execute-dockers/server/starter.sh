export AICClient0Name=$client0_id
export AICClient0Token=$client0_token
export AICClient1Name=$client1_id
export AICClient1Token=$client1_token
TIMELIMIT=360

echo 'unzip'
unzip config.zip -d config/

echo 'running'
timeout $TIMELIMIT java -jar server.jar --config=server.conf

echo 'Server terminated'
