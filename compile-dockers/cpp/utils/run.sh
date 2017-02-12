EXECUTABLE_NAME='swarm'

cd src
sudo -E -u runner -s ./$EXECUTABLE_NAME.out

echo 'Client terminated.'
