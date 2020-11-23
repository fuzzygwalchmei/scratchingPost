import requests
from bs4 import BeautifulSoup as bs

BASE = 'https://twitter.com/'

def base_scrape(handle):
    print(f'start: {handle}')
    r = requests.get(BASE+handle)
    soup = bs(r.content, features="html.parser")
    print(soup.find('div',{'data-testid':'tweet'}))

base_scrape('fuzzygwalchmei')
