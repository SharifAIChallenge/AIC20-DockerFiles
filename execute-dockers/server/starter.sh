export AICClient0Name=$client0_id
export AICClient0Token=$client0_token
export AICTeamName0=$client0_name

export AICClient1Name=$client1_id
export AICClient1Token=$client1_token
export AICTeamName1=$client1_name

export AICClient2Name=$client2_id
export AICClient2Token=$client2_token
export AICTeamName1=$client1_name

export AICClient3Name=$client3_id
export AICClient3Token=$client3_token
export AICTeamName3=$client3_name

echo 'unzip'
unzip config.zip -d config/

echo 'running'
java -jar server.jar --config=server.conf

ls
ls Log
mv Log/graphic*.json graphic.log

echo 'Server terminated'
