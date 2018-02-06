EXECUTABLE_NAME='client'

cd src
sudo -E -u runner -s client/$EXECUTABLE_NAME

echo 'Client terminated.'
