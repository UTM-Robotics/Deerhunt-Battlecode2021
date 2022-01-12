import docker
import os
from dotenv import load_dotenv
from time import sleep
import requests
from gameController import MerlinGameController
import shutil
load_dotenv()

class Consumer:
    '''Consumer retrieves matches from the submission queue, runs them and updates the leaderboard '''
    def __init__(self):
        self.api_url = os.getenv('API_URL')
        self.save_path = os.getenv('SAVE_PATH') # must have trailing slash like: /tmp/saved/
        self.token = os.getenv('TOKEN')
        self.event_id = os.getenv('EVENT_ID')
        self.event_name = os.getenv('EVENT_NAME')
        self.gameController= MerlinGameController(self.save_path)


    def run(self):
        '''run constantly checks to see if there are new submissions, if there is run the match and update the leaderboard'''
        while True:
            #Get the next match and run the match if there is one (by order of modified)
            match = None
            match = self.get_match()
            if match is not None:
                try:
                    self.match_id = match[0]['_id']
                    teams = self.get_teams(match[0])
                    print(teams)
                    for team in teams:
                        self.download_submission(team)
                    winner, loser, log_path = self.gameController.run_game(teams)
                    if log_path == None:
                        self.post_match_default(winner, loser)
                    else:
                        if winner:
                            print(winner)
                            self.post_match(winner, loser, log_path)
                        else:
                            print("Game failed to be generated, zip succeeded.")
                except Exception as e:
                    print(e)
                    print("Game result could not be generated, continueing.")
            else:
                print('sleeping 5s')
                sleep(5)

    def get_match(self):
        try:
            result = requests.get(f'http://{self.api_url}/api/requests', params={"token":self.token, "event_id": self.event_id})
            if result.status_code == 200:
                return result.json()
            else:
                return None
        except:
            print("Failure retrieving match data.")
            return None

    def download_submission(self, team):
        local_filename = f'{self.save_path}{team}.zip'
        # NOTE the stream=True parameter below
        with requests.get(f'http://{self.api_url}/api/consumer/downloads', params={"token":self.token,"team_id":team,"event_name":self.event_name}, stream=True) as r:
            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content():
                    f.write(chunk)
        return local_filename

    def zip_file(self, path):
        '''
        Zips the file and returns the filepath with the zip file.
        If crash, just crash and deal with consequences normally?
        '''
        shutil.make_archive('merlinresult', 'zip', path)


    def post_match(self, winner, loser, file_path) -> str:
        self.zip_file(file_path)
        replayfile={'file': open(f'{os.getcwd()}/merlinresult.zip','rb')}
        result = requests.post(f'http://{self.api_url}/api/match', params={"token":self.token, "event_id": self.event_id,
                                                                   'winner_id': winner, 'loser_id': loser},
                                                            files=replayfile)
        print(f'Match with winner: {winner} and loser: {loser} has been posted')
        self.gameController.clean_previous()

    def post_match_default(self, winner, loser) -> str:
        result = requests.post(f'http://{self.api_url}/api/match', params={"token":self.token, "event_id": self.event_id,
                                                                   'winner_id': winner, 'loser_id': loser})
        self.gameController.clean_previous()
    def get_teams(self, match_object):
        teams = [i['$oid'] for i in match_object["teams"]]
        return teams

if __name__ == "__main__":
    consumer = Consumer()
    consumer.run()
