'''
Created on Aug 20, 2020
@author: Brennan Brown
'''

from weather_data import get_weather_data
from create_html import create_html_report 
from email_via_gmail import send_gmail

from collections import OrderedDict
from time import sleep
from pprint import pprint
import schedule

def job():
    pprint(schedule.jobs)
    weather_dict, icon = get_weather_data('KLAX')  
    weather_dict_ordered = OrderedDict(sorted(weather_dict.items())) 
    
    email_file = "email_weather.html"
    create_html_report(weather_dict_ordered, icon, email_file)
    send_gmail(email_file)

schedule.every().hour.do(job)

while True:
    schedule.run_pending()
    sleep(1)
