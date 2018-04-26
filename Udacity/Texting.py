import time;
from twilio.rest import Client

auth_token = "d3ff8561337ef68c149b626e00ad150d"
acct_sid = "ACa640b06c93d7f780398d1c063b409265"

fromNb = "+17206055437"
toNb = "+17202392413"
msgTxt = "Hello There!"

client = Client(acct_sid, auth_token)

#message = client.sms.messages.create(msgTxt, toNb,twilioPhoneNb)
message = client.api.account.messages.create(to=toNb,from_=fromNb,body=msgTxt)

print ("Done with message call: ", message.status)
#while (message.status == "queued"):
 #   print(message.status, " :  Sleeping for 10")
  #  message.
   # time.sleep(10)

print ("Message Status is now: ", message.status)


#import twilio
#print(twilio.__version__)
#print(twilio.__version_info__)
#print("this is a newer version of this program")