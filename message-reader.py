# imports
from slackclient import SlackClient # used to send the message to slack
import json # used to get slack key from json file

# write key to json file
#x = {"key": 123456789} # insert your own key
#with open("key.json", "w") as file:
#    json.dump(x, file)

# json variables
with open("key.json", "r") as file:
    jsonfile = json.load(file)

# slack variables
slack_token = jsonfile["key"]
print(slack_token)
sc = SlackClient(slack_token)

with open("message.txt", "r") as messagefile:
    message = messagefile.read
    print(message)
    sc.api_call(
        "chat.postMessage",
        channel = "polls", # change channel variable to what channel message will be posted in
        text = message
    )
