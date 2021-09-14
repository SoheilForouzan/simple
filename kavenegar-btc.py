#!/usr/bin/env python
from kavenegar import *
import requests


def inform():
    api = KavenegarAPI('api key here') # Kavenegar api key goes here
    params = {
        'sender': 'sender num', # Sender number
        'receptor': 'receiver', # receptor number
        'message': btc
    }   
    response = api.sms_send(params)
    print('[!] sent')

link = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false').json()[0]

btc = (link['current_price'])
inform()
