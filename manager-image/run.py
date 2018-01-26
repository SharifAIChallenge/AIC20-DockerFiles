import shutil
import os
import docker
import time
import compose.config as compose_config
from compose.config.serialize import serialize_config

import logging

import subprocess

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

streamLogger = logging.StreamHandler()
streamLogger.setLevel(logging.INFO)
logger.addHandler(streamLogger)

UID_ENVIRONMENT_KEY = "MANAGER_UID"
COMPOSE_DIRECTORY = "/compose"

if __name__ == "__main__":
    manager_uid = os.environ.get("MANAGER_UID")
    listened_container = os.environ.get("MANAGER_LISTEN_SERVICE", None)

    WORKING_DIR = "/compose-fin"

    shutil.copytree(COMPOSE_DIRECTORY, WORKING_DIR)
    client = docker.from_env()
    node_id = client.info()["Swarm"]["NodeID"]
    config = compose_config.load(
        compose_config.find(
            WORKING_DIR,
            ["docker-compose.yml"],
            compose_config.environment.Environment(os.environ)
        )
    )

    services = config.services
    for service in services:
        if 'deploy' not in service:
            service['deploy'] = {}
        service['deploy']['placement'] = {}
        service['deploy']['placement']['constraints'] = ['node.id == ' + node_id]
        service['deploy']['restart_policy'] = {}
        service['deploy']['restart_policy']['condition'] = 'none'

    final_file_path = os.path.join(WORKING_DIR, 'docker-compose-final.yml')
    with open(final_file_path, 'w') as f:
        f.write(serialize_config(config))

    logger.info("Number of services: {}".format(str(len(services))))

    subprocess.call(["docker", "stack", "deploy", "-c", final_file_path,  manager_uid])

    # FIXME: Currently API doesn't support stacks. The following code assumes
    # that all objects related to a stack have a label com.docker.stack.namespace=<stack_name>
    # This is the current assumption of Docker CLI.
    while len(client.api.tasks(
            filters={"label": "com.docker.stack.namespace={}".format(manager_uid)})
    ) < len(services):
        time.sleep(0.5)

    logger.info("All services have been created")

    filters = {
        "label": "com.docker.stack.namespace={}".format(manager_uid),
        "desired-state": "shutdown",
    }

    if listened_container:
        filters["name"] = "{}_{}".format(manager_uid, listened_container)
        important_services_count = 1
    else:
        important_services_count = len(services)

    while len(client.api.tasks(
            filters=filters
    )) < important_services_count:
        time.sleep(0.5)

    logger.info("All services finished")

    logger.info("Cleaning up")

    subprocess.call(["docker", "stack", "rm", manager_uid])

    # TODO: Add graceful shutdown which jumps to cleaning up