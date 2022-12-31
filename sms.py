import os
from twilio.rest import Client
from dotenv import load_dotenv
import random

load_dotenv()

def randomize_message():
    f = open("mornings.txt","r")
    messages = []
    for message in f.readlines():
        messages.append(message.replace("\n", ""))
    rdm_message = random.choice(messages)
        
    return rdm_message
    
    
def send_messages():
 	account_sid = os.getenv("ACCOUNT_SID")
 	auth_token = os.getenv("AUTH_TOKEN")
 	client = Client(account_sid, auth_token)
 	phone_num = os.getenv("TWILIO_PHONE_NUMBER")
 	anton = os.getenv("ANTON")
 	anna = os.getenv("ANNA")

 	recipients = [anton]

 	for number in recipients:
         message = client.messages.create(
             body = randomize_message(),
             from_ = phone_num,
             to = number
        )
        
         print(message.sid)
