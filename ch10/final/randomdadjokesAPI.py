import requests

class DadJokesAPI:
    def __init__(self):
        self.api_url = "https://icanhazdadjoke.com/"
        
    def get(self):
        headers = {"Accept": "application/json"}
        response = requests.get(self.api_url, headers=headers)
        if response.status_code == 200:
            joke = response.json()["joke"]
            return joke
        else:
            return "Error: Unable to retrieve joke from Dad Jokes API"
