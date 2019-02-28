export AICClient0Name=$client0_id
export AICClient0Token=$client0_token
export AICClient1Name=$client1_id
export AICClient1Token=$client1_token

echo 'unzip'
unzip config.zip -d config/

echo 'render server.comg'
sed -e "s/TEAMNAME0/$client0_name/g" \
    -e "s/TEAMNAME1/$client1_name/g" \
    /game/server.template.conf > /game/server.conf
cat /game/server.conf

echo 'running'
java -jar server.jar --config=server.conf

echo 'Server terminated'
