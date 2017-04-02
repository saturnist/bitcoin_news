import requests
from datetime import datetime, timedelta
from api_keys import ny_api
import time


def nyt_bitcoin(start):

    results = {}
    dates = {}

    for s in start:

        s = datetime.strptime(s, '%Y-%m-%d')
        end = s + timedelta(days=1)
        s = s.strftime('%Y%m%d')
        end = end.strftime('%Y%m%d')

        dates[s] = end

    for d in dates:

        r = requests.get(f'http://api.nytimes.com/svc/search/v2/articlesearch.json?q=bitcoin&begin_date={d}&end_date={dates[d]}&api-key={ny_api}&sort=oldest')
        headlines = r.json()

        for h in headlines['response']['docs']:
            results[h['headline']['main']] = h['web_url']
        time.sleep(5)

    return results
