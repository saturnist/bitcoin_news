import requests
import json


def tobtc(currency, value):
    r = requests.get('https://blockchain.info/tobtc?currency={currency}&value={value}')
    j = json.loads(r.content)
    return j
