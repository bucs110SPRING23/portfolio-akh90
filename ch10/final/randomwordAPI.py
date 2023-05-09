import requests

class BoredAPI:
    api_url = "https://www.boredapi.com/api/activity/"

    def get(self, type=None, participants=None):
        params = {}
        if type:
            params["type"] = type
        if participants:
            params["participants"] = participants
        
        response = requests.get(self.api_url, params=params)
        data = response.json()
        return data["activity"]
        

