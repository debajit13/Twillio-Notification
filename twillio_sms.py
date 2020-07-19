from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'Enter Your SID here'
auth_token = 'Enter Your Auth Token here'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
        from_='Your Twillio Number',
        to='Number where you want to send SMS',
        body="Your Message"
    )

print(message.sid)
