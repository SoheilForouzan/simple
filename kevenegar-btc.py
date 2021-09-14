from kavenegar import *
import requests


def inform():
    api = KavenegarAPI('676631383747544A634556654D653664364D3633322F72424B52342F612B4950344A38724739766A4E36673D')
    params = {
        'sender': '10004346',
        'receptor': '9911825644',
        'message': btc
    }   
    response = api.sms_send(params)
    print('[!] sent')

link = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false').json()[0]

btc = (link)
print(btc)
#inform()