#Project Workflow
#Twillo client setup
#User Input
#scheduling logic
#Massage send

from twilio.rest import Client
from datetime import datetime,timedelta                 #Timedelta for time scheduling
import time

#Twillo account setup
account_sid='AC08527a8429b05b1287d9d5df9f95f4ee'
auth_token='cae9ec2d8c90a8b160b7633bebb6173b'

client= Client (account_sid,auth_token)



# Message send function
def send_whatsapp_message(recipient_number, message_body):
    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=message_body,
            to=f'whatsapp:{recipient_number}'
        )
        print(f'Message sent successfully! Message SID: {message.sid}')
    except Exception as e:
        print(f'An error occurred: {e}')
        

#User Input

name = input('Enter the recipient name: ')
recipient_number = input('Enter the recipient WhatsApp number with country code: ')
message_body = input(f'Enter the message you want to send to {name}: ')



# Date, time function
date_str = input('Enter the date to send message (YYYY-MM-DD): ')
time_str = input('Enter the time to send the message (HH:MM in 24 Hour Format): ')

try:
    schedule_datetime = datetime.strptime(f'{date_str} {time_str}', '%Y-%m-%d %H:%M')
except ValueError:
    print('Invalid date or time format. Please use YYYY-MM-DD for date and HH:MM for time.')
    exit(1)

current_datetime = datetime.now()
time_difference = schedule_datetime - current_datetime
delay_seconds = time_difference.total_seconds()

if delay_seconds <= 0:
    print('The specified time is in the past. Please enter a future date and time.')
else:
    print(f'Message scheduled to be sent to {name} at {schedule_datetime}.')
    # Wait until scheduled time
    time.sleep(delay_seconds)
    # Send the message
    send_whatsapp_message(recipient_number, message_body)
