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
        if not os.path.isdir(self.location):
            os.mkdir(self.location)

        self.client = docker.from_env()
        self.last_timestamp = None

    def clean_previous(self):
        print("Cleaning previous run")
        try:
            shutil.rmtree(self.client1)
        except Exception as e:
            print(e)
        try:
            shutil.rmtree(self.client2)
        except Exception as e:
            print(e)
        
        try:
            os.remove('merlinresult.zip')
        except Exception as e:
            print(e)
        try:
            os.remove(f'{self.location}{self.teams[0]}.zip')
        except Exception as e:
            print(e)
        try:
            os.remove(f'{self.location}{self.teams[1]}.zip')
        except Exception as e:
            print(e)

        try:
            shutil.copytree(self.backupclient, self.client1)
        except Exception as e:
            print(e)
        try:
            shutil.copytree(self.backupclient, self.client2)
        except Exception as e:
            print(e)
        print("cleanup complete")


    def inject_zipped(self):
        print("printing clients:")
        print(self.client1)
        print(self.client2)
        try:
            with ZipFile(f'{self.location}{self.teams[0]}.zip', 'r') as zip_file:
                zip_file.extractall(self.client1)
        except BadZipFile:
            return (0,1)# winner , loser by default
        try:
            with ZipFile(f'{self.location}{self.teams[1]}.zip', 'r') as zip_file:
                print("Success printing client1")
                zip_file.extractall(self.client2)
        except BadZipFile:
            return (1,0) # winner, loser by default
        return None# success

    def run_game(self, teams):
        self.teams = teams
        container_tag = uuid.uuid4().hex
        default = self.inject_zipped()
        if default:
            return teams[default[0]] , teams[default[1]], None # default winners, no files to upload since never ran.
        print("Running game between:", str(teams))
        self.client.images.build(path="../", tag=container_tag, rm=True)
        self.client.containers.run(container_tag, detach=False, auto_remove=True, \
            network_mode=None, cpu_count=1, mem_limit='512m', volumes=[f'{self.host_volume}:/deerhunt'])
        image = self.client.images.get(container_tag)
        self.client.images.remove(image=image.id, force=True)
        if os.path.isfile(f'{self.host_volume}/log.json') and os.path.isfile(f'{self.host_volume}/result.json'):
            with open(f'{self.host_volume}/result.json') as f:
                result = json.loads(f.read())
                print(result)
                if result['winner'] == 'p1':
                    return (teams[0], teams[1], f'{self.host_volume}')
                else:
                    return (teams[1], teams[0], f'{self.host_volume}')
        return (False, False, False)
