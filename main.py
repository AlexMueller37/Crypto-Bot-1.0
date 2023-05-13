from make_order import order
from mean_reversion import mean_reversion

import numpy as np 
import requests
from time import sleep
from datetime import datetime
import pprint
import talib

security = 'BTCUSD'
url = f'https://api.binance.us/api/v3/ticker?symbol={security}'

closes = []
in_position = False
counter = 0

TRADE_SYMBOL = 'BTCUSD'
TRADE_QUANTITY = .5

buy_price = 0
sell_price = 0

API_KEY = 'PKEACEMDMC69HGLPAKU0'
SECRET_KEY = 'SdWuBij5goM1FacHxGBVZPgfObz3X4lg2n0F5Evl'

completed_trade = False 

while True: 
    counter += 1
    response = requests.get(url)
    response = response.json()

    close = response['lastPrice']
    closes.append(float(close))

    last_price = closes[-1]

    print(f'candle closed at {close}')

    output = mean_reversion(closes, in_position)

    if output == 'buy': 
        print('Buying...')
        order(TRADE_SYMBOL, TRADE_QUANTITY, 'buy', 'market', 'gtc', API_KEY, SECRET_KEY)
        buy_price = last_price
        print('Success!')
        in_position = True
    if output == 'sell': 
        print('Selling...')
        order(TRADE_SYMBOL, ((TRADE_QUANTITY - (TRADE_QUANTITY * 0.0025)) - 0.000000001), 'sell', 'market', 'gtc', API_KEY, SECRET_KEY)
        sell_price = last_price
        print('Success!')
        completed_trade = True
        in_position = False
    if output == 'no action': 
        print('No Action Needed')

    print(f'Currently Holding : {in_position}')
    print(f'Counter : {counter}')

    if completed_trade: 
        print('----------------------------------------')
        print(f'Buy Price: {buy_price}')
        print(f'Sell Price: {sell_price}')
        print(f'Gain / Loss (Without Trading Fee) : {sell_price - buy_price}')
        sell_price = 0 
        buy_price = 0

    print('===============================================================================================================')
        
    sleep(5)