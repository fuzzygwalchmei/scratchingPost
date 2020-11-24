import requests
from bs4 import BeautifulSoup as bs
import sys
from dotenv import load_dotenv
load_dotenv()
import os



BASE = 'https://api.twitter.com/1.1/search/tweets.json?q='
handle = sys.argv[1]
BEARER_TOKEN = os.environ.get("BEARER_TOKEN")

print(f'Sys.argv: {handle}')

def base_scrape(handle):
    print(f'start: {handle}')
    print(BASE+handle)
    r = requests.get(BASE+handle, headers={'Authorization':f'Bearer {BEARER_TOKEN}'})
    print(r.content[0])
    # soup = bs(r.content, features="html.parser")
    # print(soup.find_all('div',attrs={'data-testid':'tweet'}))

base_scrape(handle)

