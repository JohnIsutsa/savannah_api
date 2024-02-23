import os
from django.core.mail import EmailMessage
from twilio.rest import Client
from dotenv import load_dotenv

class Message:

    @staticmethod
    def send_message(data):
        load_dotenv()
        account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        auth_token = os.getenv('TWILIO_AUTH_TOKEN')
        cliient = Client(account_sid, auth_token)
        
        message = cliient.messages.create(
            body=data['body'], from_=os.getenv('TWILIO_PHONE_NUMBER'), to=data['to']
        )