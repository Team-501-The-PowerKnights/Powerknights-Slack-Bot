from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import date_range as DR

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    print("Writen to file")
    events_result = service.events().list(calendarId='d52gionm3cmrhsd0b4vol77okg@group.calendar.google.com',timeMin=DR.week_range()[0],timeMax=DR.week_range()[1], singleEvents=True,orderBy='startTime').execute()

    events = events_result.get('items', [])
    #
    # event_info = []
    #
    # for event in events:
    #     start = event['start'].get('dateTime', event['start'].get('date'))
    #     event_info.append(start)
    #     event_info.append(event['summary'])

    # print(event_info) 

    with open("events.txt", "a") as events_file:
        events_file.write(events)

if __name__ == '__main__':
    pass
    main()
