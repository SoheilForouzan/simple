# Requirements
import smtplib
import requests
import time
from email.message import EmailMessage

from requests.api import request

# Fake email Info
password = 'passwd' # Sender password
#input('[?] Enter your email password >>>> ')
email = "Email" # Sender email
cryptoLink = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false"

while True:
    # Get Crypto data
    text = float(requests.get(cryptoLink).json()[0]['current_price'])
    print(f'[$] Price is : {text}')
    # Try to send the email
    try:
        msg = EmailMessage()
        msg['Subject'] = 'BTC Price'
        msg['from'] = email
        msg['to'] = 'email' # receiver email 
        msg.set_content(f'BTC Price : {text}')

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(email, password)

            smtp.send_message(msg)

        print("[+] Email Sent!")
    except:
        print('[X] Error')
    time.sleep(60)
    
