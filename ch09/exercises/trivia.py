import requests
import random


class TriviaAPI:

    def __init__(self, category=18, amount=1):
        self.url = f'https://opentdb.com/api.php?amount={amount}&category={category}'

    def get(self):
        r = requests.get(self.url)
        response = r.json()

        if response.get('results'):
            return response ['results']
        else: 
            return None
    def change_category(self, category):
        pass

def trivia():