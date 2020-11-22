import requests
from bs4 import BeautifulSoup as bs
from collections import namedtuple

Course = namedtuple('Course',['title', 'link', 'length', 'posted'])
courses = []

def get_course_info(link):
    r = requests.get(link)
    page = bs(r.content, features="html.parser")
    title = page.find('h1',{'data-purpose':'lead-title'}).text.strip()
    length = page.find('span',{'data-purpose':'video-content-length'}).text
    return title, length

def get_course_details(page):
    link = requests.get(page['href'])
    linkpage = bs(link.content, features="html.parser")
    coupon = linkpage.select('a.bbc_link')
    bbc_link = coupon[0]['href']
    posted = linkpage.select('div.smalltext')[0].text
    # udemy_links.append((bbc_link, posted))
    title, length = get_course_info(bbc_link)
    courses.append(Course(title, bbc_link, length, posted))
    print(f'{title} - Done')

def get_udemy_links():
    base = 'https://www.jucktion.com/forum/udemy-coupon/'
    last_date = 'Today'
    count = 00
    pages = []
    
    # This will get the links of each of the articles, doesnt cater for next page yet
    while any([x in last_date for x in ['Today', 'Yesterday']]) :
        r = requests.get(base+f'{count:02}')
        webpage = bs(r.content, features="html.parser")
        last_date = webpage.select('td.lastpost')[-1].text
        pages.extend(webpage.select('td.subject a'))
        print(f'Finished pages for {count:02}')
        count += 20

    # udemy_links = []
    
    for page in pages[1:]:
        get_course_details(page)
    print('pages completed')

    return udemy_links



udemylinks = get_udemy_links()

print(courses)