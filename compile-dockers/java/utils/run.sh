cd src/src
sudo -E -u runner -s java -classpath .:../:/libs/gson-2.3.1.jar client.Main

echo 'Client terminated.'
