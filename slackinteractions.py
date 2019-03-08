import pytz
import httplib2
import requests

from datetime import datetime, timedelta
from apiclient.discovery import build
from oauth2client.client import SignedJwtAssertionCredentials

with open('calendarchecker.p12', 'rb') as f:
  key = f.read()

service_account_name = #EMAIL ADDRESS IN OAUTH SERVICE ACCOUNT

credentials = SignedJwtAssertionCredentials(
service_account_name, key,
scope=['https://www.googleapis.com/auth/calendar',
'https://www.googleapis.com/auth/calendar.readonly'])

http = httplib2.Http()
http = credentials.authorize(http)

service = build(serviceName='calendar', version='v3', http=http)

showDeleted = True

lists = service.calendarList().list().execute()
pprint.pprint(lists)

page_token = None
while True:
  events = service.events().list(calendarId=service_account_name, pageToken=page_token).execute()
  pprint.pprint(events)
  for event in events['items']:
    print event['summary']
  page_token = events.get('nextPageToken')
  if not page_token:
    break
