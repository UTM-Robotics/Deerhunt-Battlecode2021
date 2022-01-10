import docker
import os
from dotenv import load_dotenv
from time import sleep
import requests

load_dotenv()

class Consumer:
    '''Consumer retrieves matches from the submission queue, runs them and updates the leaderboard '''
    def __init__(self):
        self.api_url = os.getenv('API_URL')
        self.save_path = os.getenv('SAVE_PATH')
        self.token = os.getenv('TOKEN')
        self.event_id = os.getenv('EVENT_ID')
    def run(self):
        '''run constantly checks to see if there are new submissions, if there is run the match and update the leaderboard'''
        while True:
            #Get the next match and run the match if there is one (by order of modified)
            match = None
            match = self.get_match()
            if match is not None:
                try:
                    teams = self.get_teams(match)
                    for team in range(len(teams)):
                        self.download_submission(teams[team])
                    result_dict, files = GameController.run_game()
                    self.post_match(result_dict, files)
                except Exception as e:
                    print(e)
                    print("Game result could not be generated, continueing.")
            else:
                sleep(15)

    def get_match(self):
        try:
            result = requests.get(url=self.api_url +"/requests", params={"token":self.token, "event_id": self.event_id})
            if result.status_code == 200:
                return result.json()
            else:
                return None
        except:
            print("Failure retrieving match data.")
            return None

    def download_submission(self, team):


    def zip_file(self, file):
        '''
        Zips the file and returns the filepath the the zip file. if crash, just crash and deal with consequences normally?
        '''
        
    def post_match(self, winner, loser, file_path) -> str:
        f = open(file_path)
        data = {}
        result = requests.post(url=self.api_url +"/requests", params={"token":self.token, "event_id": self.event_id})

    def get_teams(self, match_object):
        teams = match_object["teams"]
        return teams
if __name__ == "__main__":
    consumer = Consumer()
    consumer.run()