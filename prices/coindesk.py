import requests
import json


def btc_interval(start, end):

    start_hyphen = f'{start[0:4]}-{start[4:6]}-{start[6:]}'
    end_hyphen = f'{end[0:4]}-{end[4:6]}-{end[6:]}'
    r = requests.get(f'https://api.coindesk.com/v1/bpi/historical/close.json?start={start_hyphen}&end={end_hyphen}')
    j = json.loads(r.content)
    return j
