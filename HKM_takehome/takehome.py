import requests
from bs4 import BeautifulSoup as bs
import sys
from dotenv import load_dotenv
load_dotenv()
import os
import json



BASE = 'https://api.twitter.com/1.1/search/tweets.json?q='
handle = sys.argv[1]
BEARER_TOKEN = os.environ.get("BEARER_TOKEN")

print(f'Sys.argv: {handle}')

def base_scrape(handle):
    print(f'start: {handle}')
    print(BASE+handle)
    r = requests.get(BASE+handle+'&f=live', headers={'Authorization':f'Bearer {BEARER_TOKEN}'})

    page = json.loads(r.content)
    try:
        for i in range(15):
            print(page['statuses'][i]['text'])
    except:
        print('Nothing New')


base_scrape(handle)

# api stream/rules where authorid  == supplied handle?
# get user id from supplied handle
# store in some sort of list/dict? compare timestamps or tweet id, only print new ones
