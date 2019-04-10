try:
    with open("slack_token.txt") as slack_token_file:
        slacktoken_invalid = str(slack_token_file.read())
        slacktoken = slacktoken_invalid.strip("\n")

except FileNotFoundError:
    print("Please make the slack_token.txt file and put your API key in it")

channels = {
           "polls":"CE36EEKA9",
           }


import os
from slackclient import SlackClient

sc = SlackClient(slacktoken)

sc.api_call(
  "chat.postMessage",
  channel="CE36EEKA9",
  text="Testing Testing",
  as_user="false"
)
