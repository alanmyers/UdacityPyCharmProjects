import time;
import configparser
config = configparser.ConfigParser()

config.read(r"C:\Users\amyer\PycharmProjects\Udacity\texter.ini")

from twilio.rest import Client

auth_token = config['DEFAULT']['auth_token']
acct_sid = config['DEFAULT']['acct_sid']

fromNb = config['DEFAULT']['fromNb']
toNb = config['DEFAULT']['toNb']
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

print ("Changed remotely")
x = 4 / 2 
print ("4 / 2 = ", x)


#import twilio
#print(twilio.__version__)
#print(twilio.__version_info__)
#print("this is a newer version of this program")
