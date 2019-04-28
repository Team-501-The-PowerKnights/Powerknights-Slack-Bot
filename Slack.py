import os
from slackclient import SlackClient

try:
    with open("slack_token.txt") as slack_token_file:
        slacktoken_invalid = str(slack_token_file.read())
        slacktoken = slacktoken_invalid.strip("\n")
except FileNotFoundError:
    print("Please make the slack_token.txt file and put your Slack API key in it")

channels = {
           "polls":"CE36EEKA9",
           "general":"C5DEPCK24",
           "bot-dev":"CGE8GGJ0G",
           }

sc = SlackClient(slacktoken)


def send_message(channel_loc,message,get_info):
    """
    Bot will send a message to Slack
    :param channel where the message wants to be send.
        :type str
    :param message that wants to be sent to Slack
        :type str
    :param see return
        :type boolean
    :return will return the action's data only if get_info is True
        :type dictonary
    """
    action = sc.api_call(
    "chat.postMessage",
    channel=channel_loc,
    text=message,
    as_user="false"
    )
    if action["ok"]:
        print("Message has been posted")
    elif not action["ok"]:
        print("Message error. Please make sure that the message has been writen to the message.txt file")
    if get_info:
        return action


def emoji_react(emoji,message,get_info):
    """
    Bot will react with an emoji to a message in Slack
    :param emoji that will be reacted
        :type string
    :param message that was posted using this bot to react too
        type: dictonary
    :param see return
        :type boolean
    :return will return the action's data only if get_info_is True
        :type
    """
    action = sc.api_call(
    "reactions.add",
    channel=message["channel"],
    name=emoji,
    time_stamp = message['ts'],
    )
    if get_info:
        return action

message_from_file = "Testing Testing"

response = send_message(channels["bot-dev"],message_from_file,True)
emoji_reaction = emoji_react("thumbsup",response,False)
