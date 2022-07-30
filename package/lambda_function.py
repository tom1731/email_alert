import os
import smtplib
from email.message import EmailMessage

import requests
from bs4 import BeautifulSoup

def lambda_handler(event, context):
    EMAIL_ADDRESS = "tomgun.quechua@gmail.com"
    EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

    url = 'https://fanatec.com/eu-en/racing-wheels-wheel-bases/wheel-bases/csl-dd-5-nm'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    if not soup.find_all(class_='delivery--text-not-available'):
        msg = EmailMessage()
        msg['Subject'] = "csl dd available !!!!!!!!!"
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = ['tom.desire17@gmail.com']
        msg.set_content('csl dd available !!!!!!!!!')
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, 'EMAIL_PASSWORD')
            smtp.send_message(msg)
    else:
        msg = EmailMessage()
        msg['Subject'] = "Test email!"
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = ['tom.desire17@gmail.com']
        msg.set_content('lambda function is still working')
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, 'EMAIL_PASSWORD')
            smtp.send_message(msg)
