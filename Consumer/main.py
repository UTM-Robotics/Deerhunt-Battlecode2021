import docker
import os
from dotenv import load_dotenv
from time import sleep
load_dotenv()

class Configuration:

    # Saving flask specific env
    TESTING = os.getenv('TESTING')
    CONSUMER_TOKEN = os.getenv("CONSUMER_TOKEN")
    

class Consumer:
    '''Consumer retrieves matches from the submission queue, runs them and updates the leaderboard '''
    def __init__(self):
        api_url = ""
        pass
    def run(self):
        '''run constantly checks to see if there are new submissions, if there is run the match and update the leaderboard'''
        while True:
            #Get the next match and run the match if there is one (by order of modified)
            match = self.submission_queue.find_one(sort=[("modified", 1)])
            if match is not None:
                print("Got match")
                try:
                    self.submission_queue.delete_one({'_id': match['_id']})
                    #Runs the match and gets the result
                    match_string = self.create_match(match)
                    if match_string is not None and not isinstance(match_string, int):
                        print("got match {}".format(match_string))
                        result = GameController.run_game(match_string)
                        self.database.logs.insert_one({"winner": result[1], "data": result[0], "team_id": self.challenger['_id'], "modified": datetime.now()})
                    elif match_string is None:
                        return
                    elif match_string == StorageAPI.P1_ZIP_ERROR: # Handle invalid zip file.
                        print("Got bad match")
                        match_result = {'lines': [],
                            'maps': [],
                            'errors': [],
                            'build_id': []
                            }
                        result = (match_result,1)
                        self.update_leaderboard(result)
                    #Removes the match from the submission queue
                except FileNotFoundError:
                    print("File not found {}".format(self.challenger['_id']))
            else:
                sleep(5)
                
    
    def post_match(self, match: dict) -> str:
        '''Posts the match results given a match request.'''
        #Gets the 2 players from db object
        self.challenger = self.teams.find_one({"_id": match['challenger_id']})
        self.defender = self.teams.find_one({"_id": match['defender_id']})
        
        #Verifies
        if self.challenger is None or self.defender is None:
            print("Challenger or defender do not exist")
            return

        if self.challenger == self.defender:
            print("Can not challenge own team")
            return

        return StorageAPI.prep_match_container(self.defender['_id'], self.challenger['_id'])

    def update_leaderboard(self, result: tuple):

if __name__ == "__main__":
    consumer = Consumer()
    consumer.run()