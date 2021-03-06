#!/usr/bin/env python
import google_cal as GC
import slack as SL
import message_creator as MC
from slackclient import SlackClient


try:
    with open("./secrets/slack_token.txt") as slack_token_file:
        slacktoken_invalid = str(slack_token_file.read())
        slacktoken = slacktoken_invalid.strip("\n")
except FileNotFoundError:
    print("Please make the slack_token.txt file and put your Slack API key in it")

sc = SlackClient(slacktoken)

channels = {
    "polls": "CE36EEKA9",
    "general": "C5DEPCK24",
    "bot-dev": "CGE8GGJ0G",
}


def main():
    """
    Will run the entire program
    """
    # Events from google calendar:
    events = GC.get_events()

    message_info = MC.create_message(events, True)
    message_to_post = message_info[0]
    emojis = message_info[1]

    # Post message to Slack
    posted_message = SL.send_message(
        sc, channels["bot-dev"], message_to_post, True)

    # React the emojis to Slack
    for emoji in emojis:
        SL.emoji_react(sc, emoji, posted_message, False)

    correct_message = input("Did the message look ok in the #polls channel? If you answer with 'y' it will be posted in the polls channel. If you answer 'gen' it will be posted in general. If you answer with 'n' or anything other than the commands shown before, then it will be stopped and not posted any where else.\n")

    if "gen" in correct_message.lower():
        posted_message = SL.send_message(
            sc, channels["general"], message_to_post, True)
        for emoji in emojis:
            SL.emoji_react(sc, emoji, posted_message, False)
    elif "y" in correct_message.lower():
        posted_message = SL.send_message(
            sc, channels["polls"], message_to_post, True)
        for emoji in emojis:
            SL.emoji_react(sc, emoji, posted_message, False)


main()
