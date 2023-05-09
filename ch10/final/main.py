from randomdadjokesAPI import DadJokesAPI
from randomwordAPI import BoredAPI

joke_api = DadJokesAPI()
activity_api = BoredAPI()

joke = joke_api.get()
activity = activity_api.get()

print(f"{joke} Was that a bad dad joke? Don't have a dad? Here's an activity to do to make up for it..hopefully:  {activity}?")


