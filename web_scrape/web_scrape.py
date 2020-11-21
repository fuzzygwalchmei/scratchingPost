import requests
from bs4 import BeautifulSoup as bs


courses = {}

def get_udemy_links():
    base = 'https://www.jucktion.com/forum/udemy-coupon/'
    
    last_date = 'Today'
    count = 00
    pages = []
    # This will get the links of each of the articles, doesnt cater for next page yet
    while 'Today' in last_date or 'Yesterday' in last_date:
        r = requests.get(base+f'{count:02}')
        webpage = bs(r.content, features="html.parser")
        last_date = webpage.select('td.lastpost')[-1].text
        pages.extend(webpage.select('td.subject a'))
        print(f'Finished pages for {count:02}')
        count += 20

    udemy_links = []
    
    print(pages[0])
    for page in pages[1:]:
        link = requests.get(page['href'])
        linkpage = bs(link.content, features="html.parser")
        coupon = linkpage.select('a.bbc_link')
        print(coupon)
        bbc_link = coupon[0]['href']
        posted = linkpage.select('div.smalltext')[0].text
        udemy_links.append((bbc_link, posted))
        print(f'{bbc_link} - Done')
    print('pages completed')

    return udemy_links

def get_course_info(link):
    r = requests.get(link)
    page = bs(r.content, features="html.parser")
    course = {}
    course['title'] = page.find('h1',{'data-purpose':'lead-title'}).text.strip()
    course['length'] = page.find('span',{'data-purpose':'video-content-length'}).text
    return course

udemylinks = get_udemy_links()
for link in udemylinks:
    courses[link] = get_course_info(link[0])

print(courses)