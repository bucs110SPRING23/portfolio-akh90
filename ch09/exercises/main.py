
# network programming

# Build a program that asks trivia questions

# server: any computer listening to network connections

# request: an incoming connection that asks from some resource from the server 
# -imgaes, video, music
# -text 
# -JSON
# -HTML


# -GET -read operation
# - visiting a page, downloading a file, etc

# -PUT -write operation(requires security)
# -login, deleting

# headers
# sent with request and the response 
# -status codes
#       -200: ok, everything went fine
#       -400: resource cannot be delieverd (404: not found)
#       -500: bad code on the server

# -IP address
# -system information (geolocation)

## urllib

#requests

#API: application programmer's interface
#APIS can return data in any format, usually it returns in JSON

#URL parameters
# ?: everthing after it is variables, 
# &

# binghamton.edu/cs?var1=100&var2=Hello

import requests
import random


class TriviaProxyAPI:

    def __init__(self):
        self.url = "https://opentdb.com/api.php?"
        self.varstr = "amount=1"

    def get (self):
        url = self.url = self.varstr
        response = requests.get(url)
        data = response.json()
        return data ['results']
    
    def csquestions (self):
        self.varstr = "amount=2&category=18"
        return self.get()
    
    def general(self):
        self.varstr = "amount=2"
        return self.get()
    


def main():
    tp = TriviaProxyAPI
    response = tp.get()


    response = requests.get("https://opentdb.com/api.php?amount=1")
    #print(response.status_code)
    #print(response.json())
    data = response.json()
    results = data['results']

    for r in results:
        print(r['questions'])
        possibles = [r["correct_answer"]] + r["incorrect_answers"]
        random.shuffle(possibles)
        input("make your selection")
        for i, p in enumerate (possibles):
            print(f"{i}) {p}")

        selection = int(input(": "))
        if possibles [selection] == r["correct_answer"]:
            print ("u r correct!")
        else:
            print("boooo! the correct answer is: {r['correct_answer]}")

                                             

main()