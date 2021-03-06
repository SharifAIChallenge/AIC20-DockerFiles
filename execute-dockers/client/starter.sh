export AICDeploy=true
export AICHostIP=server
export AICHostPort=7099
export AICToken=$token
export AICRetryDelay=5000

unzip client.zip -d client/

chown -R runner:runner client

cd client
bash run.sh 2>&1 | tee -a /game/client.tmp.log
tail /game/client.tmp.log -c 10000000 > /game/client.log

echo 'Client terminated.'
