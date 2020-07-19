from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC6c8a8f25987021640c13e9548d3a6c10'
auth_token = '2dd710ce2d9ca1930d42ede8fe561975'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
        from_='+13238701850',
        to='+918768881443',
        body="Flood alert"
    )

print(message.sid)
