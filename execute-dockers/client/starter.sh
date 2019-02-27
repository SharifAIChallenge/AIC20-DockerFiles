export AICDeploy=true
export AICHostIP=server
export AICHostPort=7099
export AICToken=$token
export AICRetryDelay=5000

unzip client.zip -d client/

chown -R runner:runner client

cd client
#sudo -E -u runner -s /bin/bash run.sh
/bin/bash run.sh | tail -c 10000000 | tee -a /game/client.log

echo 'Client terminated.'
