# Dockerfiles
Dockerfiles to build images for AIC20 

# How to use aic images

You can use ansible playbooks written in: [AIC-GameRunnerManager](https://github.com/SharifAIChallenge/AIC-GameRunnerManager)

But manually:
(Change all example.com to master ip)

### Build images

build images with commands bellow:
```
docker build compile-dockers/cpp -t example.com/aic_cpp_image
docker build compile-dockers/py3 -t example.com/aic_py3_image
docker build compile-dockers/go -t example.com/aic_go_image
docker build compile-dockers/java -t example.com/aic_java_image

docker build execute-dockers/client -t example.com/aic_client_image
docker build execute-dockers/server -t example.com/aic_server_image

docker build manager-image -t example.com/aic_manager_image
```

### Push images

Be sure registery is available.
push images with command:
```.env
docker push example.com/aic_****_image
```

## Add image usage to [AIC-GameRunner](https://github.com/SharifAIChallenge/AIC-GameRunner)

Use current [database dump](game_dump.json) using command:
```
./manage.py loaddata game_dump.json
```
And finally change exmaple.com


or manually:

[Config Manager](MANAGER.md)

[Config Compile](COMPILE.md)

[Config Run](RUN.md)


