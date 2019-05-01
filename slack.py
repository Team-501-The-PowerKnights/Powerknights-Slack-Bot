import os
from slackclient import SlackClient


def send_message(key, channel_loc,message,get_info):
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
    sc = key
    action = sc.api_call(
    "chat.postMessage",
    channel=channel_loc,
    text=message,
    as_user="false"
    )
    if action["ok"]:
        print("Poll has been posted")
    elif not action["ok"]:
        print("Error posting message")
    if get_info:
        return action


def emoji_react(key, emoji,message,get_info):
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
    sc = key
    action = sc.api_call(
    "reactions.add",
    channel=message["channel"],
    name=emoji,
    timestamp = message['ts'],
    )
    if get_info:
        return action


# Testing:
# message_from_file = "Testing Testing"
# try:
#     with open("slack_token.txt") as slack_token_file:
#         slacktoken_invalid = str(slack_token_file.read())
#         slacktoken = slacktoken_invalid.strip("\n")
# except FileNotFoundError:
#     print("Please make the slack_token.txt file and put your Slack API key in it")
# sc = SlackClient(slacktoken)
# channels = {
#            "polls":"CE36EEKA9",
#            "general":"C5DEPCK24",
#            "bot-dev":"CGE8GGJ0G",
#            }
#
# response = send_message(sc, channels["bot-dev"],message_from_file,True)
# emoji_reaction = emoji_react(sc, "thumbsup",response,False)
