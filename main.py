import config
from twilio.rest import Client

account_sid = config.ACCOUNT_SID
auth_token = config.AUTH_TOKEN
twilio = config.TWILIO
my_no = config.MY_NO
client = Client(account_sid, auth_token)

message = client.messages.create(from_=twilio, body="Hellooooow", to=my_no)