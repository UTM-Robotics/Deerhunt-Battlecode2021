from docker.types import Mount
import docker
import uuid
import os

client = docker.from_env()

container_tag = uuid.uuid4().hex

client.images.build(path="../", tag=container_tag, rm=True)

container = client.containers.run(container_tag, detach=False,auto_remove=True, \
     network_mode=None, cpu_count=1, mem_limit='512m', volumes=['/tmp/deerhunt:/deerhunt'])


while True:
    res = os.listdir('test')
    if res != []:
        print(res)
        break
