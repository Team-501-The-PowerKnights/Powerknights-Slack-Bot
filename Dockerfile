FROM python:3.6-stretch

RUN pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

COPY . .

# Remove creds if copied over (just to be safe)
RUN rm -rf secrets
RUN mkdir secrets

CMD [ "python3", "main.py" ]