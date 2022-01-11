import docker
import uuid
import os
import random
import string
import json
import shutil
from zipfile import ZipFile, BadZipFile


class GameController():
    def clean_previous(self):
        raise NotImplementedError
    def inject_zipped(self, teams):
        raise NotImplementedError
    def run_game(self):
        raise NotImplementedError

class MerlinGameController(GameController):

    def __init__(self, saved_location):
        self.location = saved_location
        self.host_volume = '/tmp/Merlin'

        os.chdir('../Merlin/client')
        self.client1 = os.getcwd()
        if not os.path.isdir('../client2'):
            shutil.copytree('.', '../client2')
        os.chdir('../client2')
        self.client2 = os.getcwd()
        if not os.path.isdir('../../Consumer/backupclient'):
            shutil.copytree('.', '../../Consumer/backupclient')
        os.chdir('../../Consumer/backupclient')
        self.backupclient = os.getcwd()
        os.chdir('..')

        self.client = docker.from_env()

    def clean_previous(self, teams):
        shutil.rmtree(self.client)
        shutil.rmtree(self.client2)
        os.remove(f'{self.location}{teams[0]}.zip')
        os.remove(f'{self.location}{teams[1]}.zip')
        shutil.copytree(self.backupclient, self.client)
        shutil.copytree(self.backupclient, self.client2)


    def inject_zipped(self):
        try:
            with ZipFile(f'{self.location}{self.teams[0]}.zip', 'r') as zip_file:
                zip_file.extractall(self.client1)
            with ZipFile(f'{self.location}{self.teams[1]}.zip', 'r') as zip_file:
                zip_file.extractall(self.client2)
        except BadZipFile:
            return False
        return True

    def run_game(self, teams):
        self.teams = teams
        container_tag = uuid.uuid4().hex
        self.inject_zipped()
        self.client.images.build(path="../", tag=container_tag, rm=True)
        self.client.containers.run(container_tag, detach=False, auto_remove=True, \
            network_mode=None, cpu_count=1, mem_limit='512m', volumes=[f'{self.host_volume}:/deerhunt'])
        image = self.client.images.get(container_tag)
        self.client.images.remove(image=image.id)
        if os.path.isfile(f'{self.host_volume}/log.json') and os.path.isfile(f'{self.host_volume}/result.json'):
            if self.last_timestamp == None:
                self.last_timestamp = os.path.getmtime(f'{self.host_volume}/result.json')
            else:
                if self.last_timestamp == os.path.getmtime(f'{self.host_volume}/result.json'):
                    return (False, False, False)
            with open(f'{self.host_volume}/result.json') as f:
                result = json.loads(f.read())
                if result['winner'] == 'p1':
                    return (teams[0], teams[1], f'{self.host_volume}/log.json')
                elif result['winner'] == 'p2':
                    return (teams[1], teams[0], f'{self.host_volume}/log.json')
        return (False, False, False)
