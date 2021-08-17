import requests
import time
import datetime
while True:

    response = requests.get(
        'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false').json()[0]

    now = datetime.datetime.now()

    print("Crypto: ", response['id'], "\n")
    print("Live Price: ", response['current_price'], "\n")
    print("Market cap: ", response['market_cap'], "\n")
    print("Price Change: ",
          response['price_change_percentage_24h'], '\n' + '-'*40)
    print(str(now))
    time.sleep(60)
