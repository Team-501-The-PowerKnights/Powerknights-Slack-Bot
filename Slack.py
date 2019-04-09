import os
from slackclient import SlackClient

slack_token = os.environ["xoxb-184987142247-559044913892-m4yXOmQYgtSC4Li0nGqjuwGA"]
sc = SlackClient(slack_token)

sc.api_call(
  "chat.postMessage",
  channel="bot-dev",
  text="Testing Testing"
)
