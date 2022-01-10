from docker.types import Mount
import docker
import uuid
import os
class GameController():
    def clean_previous(self):
        raise NotImplementedError
    def inject_zipped(self, teams):
        raise NotImplementedError
    def run_game(self):
        raise NotImplementedError

class MerlinGameController(GameController):
    def clean_previous(self):
        raise NotImplementedError
    def inject_zipped(self, teams):
        raise NotImplementedError
    def run_game(self):
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
