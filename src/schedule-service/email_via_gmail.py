'''
Created on Aug 20, 2020
@author: Brennan Brown
'''

# NOTE: Might have to be logged into your email account and also have 'Allow access for less secure apps' turned ON
# https://www.google.com/settings/security/lesssecureapps
# from within Settings: https://myaccount.google.com/security?utm_source=OGB#connectedapps

import smtplib
from email.mime.text import MIMEText
from datetime import datetime          
from GMAIL_PWD import GMAIL_PWD     

def send_gmail(msg_file):
    with open(msg_file, mode='rb') as message:              # Open report html file for reading
        msg = MIMEText(message.read(), 'html', 'html')      # Create html message
    
    EMAIL = 'mail.dev.python@gmail.com'
    msg['Subject'] = 'Hourly Weather {}'.format(datetime.now().strftime("%Y-%m-%d %H:%M"))
    msg['From'] = EMAIL
    msg['To'] = EMAIL     # NO list!       
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', port=587)
        server.ehlo()       # Extended Hello
        server.starttls()   # Put the SMTP connection in TLS (Transport Layer Security) mode.  
        server.ehlo()       # All SMTP commands that follow will be encrypted.
        server.login(EMAIL, GMAIL_PWD)
        server.send_message(msg)
        server.close()
        print("Mail was sent successfully!")
    except:
        print('An error occured during server connection.')

#===========================================
if __name__ == '__main__':
    try:
        from weather_data import get_weather_data
        from create_html import create_html_report 
        weather_dict, icon = get_weather_data('KLAX')    
        email_file = "email_weather.html"
        create_html_report(weather_dict, icon, email_file)
        send_gmail(email_file)
        print("Document generated successfully!")
    except:
        print("An error occured during document generation.")
