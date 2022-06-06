import config
from twilio.rest import Client

account_sid = config.TWILIO_ACCOUNT_SID
auth_token = config.TWILIO_AUTH_TOKEN
twilio = config.TWILIO_NO
my_no = config.MY_PHONE_NO
client = Client(account_sid, auth_token)

message = client.messages.create(
	from_=twilio,
	body="Hellooooow",
	to=my_no)


print(message.sid)