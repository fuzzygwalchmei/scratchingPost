import requests
from bs4 import BeautifulSoup as bs

r = requests.get('https://www.jucktion.com/forum/udemy-coupon/')

webpage = bs(r.content)

# This will get the links of each of the articles, doesnt cater for next page yet
pages = webpage.select('td.subject a')
for page in pages:
    print(page['href'])