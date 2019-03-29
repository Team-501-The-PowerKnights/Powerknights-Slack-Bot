# Slack-bot
Slack bot that will take all events under a certain calendar for the next week and set up a poll like system to see who is coming which days

## Modules Needed:
* slackclient
* datetime
* pickle
* os
* google modules

## API Tokens Needed:
* Slack
* Google Calendar

## What it does:
1. date_range.py (functions)
    1. RFC 3339 time stamps for the start and end of the week
2. Google_Cal.py
    1. Gets an array of all the events for a certain week
    2. Writes the array to a text file called events.txt
3. Message_Creator.py
    1. Reads events from events.txt
    2. Creates a message
    3. Writes message to message.txt
4. slackinteractions.py
    1. Reads the message from message.txt
    2. Posts message to slack channel
