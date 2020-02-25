# Config run
#### Config run images for AIC_GameRunner

in AIC_GameRunner admin:

Add new operation in  
`Home › Game › Operations`

Game: [Select Game]  
Name: `run`  
Docker compose yml template: [run template](execute-dockers/run.yml)  
Manager Service: `server` (job ends when server terminates)
Time limit: `300` (Change if required)

Also add all parameters which appeared in docker compose except `{{ server_jar }}` and `{{ server_conf }}`.

Finally add [server.conf](execute-dockers/server.conf) to operation resources with name `server_conf`.  
And add `server.jar` to operation resources too with name `server_jar`,  
Operation resources path:  
`Home › Game › Operation resources`
