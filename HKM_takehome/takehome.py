import requests
from bs4 import BeautifulSoup as bs
import sys
import os
import json


BEARER_TOKEN='AAAAAAAAAAAAAAAAAAAAAM0cKAEAAAAAJEETJhl60ORBX6ShtafU8rsp%2Fqo%3DGD1VotvsfTqdhO5RHKmxCvelprFfIzHcMeaG4qU3KqIq4zD0hG'
BASE = 'https://api.twitter.com/'
handle = sys.argv[1]


print(f'Sys.argv: {handle}')

def get_user_id(handle):
    user = requests.get(BASE+f'2/users/by/username/{handle}', headers={'Authorization':f'Bearer {BEARER_TOKEN}'})
    user = json.loads(user.content)
    user_id = user['data']['id']
    print(user_id)

def base_scrape(handle):
    print(f'start: {handle}')
    print(f'{BASE}1.1/search/tweets.json?q={handle}')
    r = requests.get(f'{BASE}1.1/search/tweets.json?q={handle}', headers={'Authorization':f'Bearer {BEARER_TOKEN}'})

    page = json.loads(r.content)
    try:
        for i in range(15):
            print(page['statuses'][i]['text'])
    except:
        print('Nothing New')

get_user_id(handle)
base_scrape(handle)

# api stream/rules where authorid  == supplied handle?
# get user id from supplied handle
# store in some sort of list/dict? compare timestamps or tweet id, only print new ones
