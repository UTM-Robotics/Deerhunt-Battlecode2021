import docker
import uuid

client = docker.from_env()
container_tag = uuid.uuid4().hex

client.images.build(path="../", tag=container_tag, rm=True)

container = client.containers.run( container_tag, detach=False,auto_remove=True, \
    network_mode=None, cpu_count=1, mem_limit='512m', volumes=['/tmp/deerhunt:/deerhunt'])

x = client.images.get(container_tag)

client.images.remove(image=x.id)

print(f'deleted imaged {x.id}')
# while True:
#     res = os.listdir('test')
#     if res != []:
#         print(res)
#         break
