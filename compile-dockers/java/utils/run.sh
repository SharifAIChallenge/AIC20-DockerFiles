cd src/src
sudo -E -u runner -s java -classpath .:../:/libs/gson-2.3.1.jar:/libs/lombok-1.18.10.jar Client.Main

echo 'Client terminated.'
