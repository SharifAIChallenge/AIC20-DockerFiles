# Config Compile
#### Config compile images for AIC-GameRunner

in AIC-GameRunner admin:

Add new operation in  
`Home › Game › Operations`

Game: [Select Game]  
Name: `compile`  
Docker compose yml template: [compile template](compile-dockers/compile.yml)  
Manager Service: `compile` (job ends when compile terminates)
Time limit: `120` (Change if required)

Also add all parameters which appeared in docker compose template.
