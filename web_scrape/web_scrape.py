import requests
from bs4 import BeautifulSoup as bs


courses = {}

def get_udemy_links():
    r = requests.get('https://www.jucktion.com/forum/udemy-coupon/')
    webpage = bs(r.content, features="html.parser")
    # This will get the links of each of the articles, doesnt cater for next page yet
    pages = webpage.select('td.subject a')

    udemy_links = []

    for page in pages[1:]:
        link = requests.get(page['href'])
        linkpage = bs(link.content, features="html.parser")
        coupon = linkpage.select('a.bbc_link')
        bbc_link = coupon[0]['href']
        udemy_links.append(bbc_link)
    print('pages completed')
    return udemy_links

def get_course_info(link):
    r = requests.get(link)
    page = bs(r.content, features="html.parser")
    course = {}
    course['title'] = page.find('h1',{'data-purpose':'lead-title'}).text.strip()
    course['length'] = page.find('span',{'data-purpose':'video-content-length'}).text
    print(course)
    return course

udemylinks = get_udemy_links()
for link in udemylinks:
    courses[link] = get_course_info(link)

print(courses)