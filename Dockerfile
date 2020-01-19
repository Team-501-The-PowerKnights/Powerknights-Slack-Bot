FROM python:3.6-stretch

# Install dependencies
RUN pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
RUN pip3 install slackclient

COPY . .

# Remove creds if copied over (just to be safe)
RUN rm -rf secrets
RUN mkdir secrets

CMD [ "python3", "main.py" ]