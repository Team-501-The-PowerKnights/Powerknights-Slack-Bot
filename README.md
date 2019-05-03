# FRC 501 The PowerKnights Slack Bot

## Description
The PowerKnights Slack Bot serves as a service to automate simple tasks in our team's Slack environment. One of the goals when making this bot was to make it using modularity so that we can easily add features over time. Over time I hope to add more functionality like getting the scores for matches from the Blue Alliance API.

## Features
At the moment the PowerKnights Slack bot only has one function. That function is to get all of the events for the current week from a calendar in Google Calendar and post a poll like a message to Slack.


## Missing Files
There are a few missing files that are used for the API tokens. Those files are slack_token.txt and credentials.json. slack_token.txt should have the oauth token for the slack bot and the credentials.json should be the credentials downloaded when you setup the google calendar API.

## Modules
If you already have pip installed on your machine, you can just run the dependencies shell file by typing `sh dependencies.sh` when in this directory and it will install all the dependencies for you.
* google-api-python
* google-auth-httplib2
* google-auth-oauthlib
* slackclient


## Files
File Name | Purpose
--------- | -------
date_range.py | Get the ISO formatted string that is the start and end date of the week.
dependencies.sh | Will install all the modules needed for this project.
google_cal.py | Gets all the events from the google calendar for the week.
message_creator.py | Creates the message that will be posted to slack. It writes the message to message.txt
slack.py | Interacts with the Slack environment. It will post a message and react to a message.
utility_functions.py | Functions that are used by other files that don't really relate. to any one specific file.
message.txt | Hosts a space for all the strings to be joined and placed in one file.
slack_token.txt | Slack bot token for interactions with the Slack environment to be authenticated.
token.pickle | Place for the google api token to be stored. Once this is created, credentials.json no longer needs to exist.


## Road Map
* TBA connection to get the results of FRC matches for the team automatically.
* Add GUI elements
* Compose messages using blocks

## Contributors
* Matthew Gleich
