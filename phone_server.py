#usr/bin/env python3
'''
__author__ = ' abba y abdullahi , abbayabdullahi68@gmail.com'

'''
from twilio.rest import TwilioRestClient



account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token = "your_auth_token"
client = TwilioRestClient(account_sid, auth_token)

call = client.calls.get("CA42ed11f93dc08b952027ffbc406d0868")
print(call.to)

