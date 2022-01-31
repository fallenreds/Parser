import requests
import lxml
from bs4 import BeautifulSoup


def get_session(url, headers, data):
    session = requests.Session()
    session.headers.update({'Referer': url})
    session.headers.update(headers)
    response = session.post(url, data=data, headers=headers)
    return session


def final_session(session):
    cookies_dict = [
        {"domain": key.domain,
         'name': key.name,
         'path': key.path,
         'value': key.value}
        for key in session.cookies]
    session2 = requests.Session()

    for cookies in cookies_dict:
        session2.cookies.set(**cookies)
    return session2


def get_name(main_div):
    name_list = []
    for i in main_div:
        href = i.find('a').text
        name_list.append(href)
    return name_list


def print_name(main_div):
    for i in main_div:
        href = i.find('a').text
        print(href)


def get_href(main_div):
    for i in main_div:
        href = i.find_all('a')
        for link in href:
            buf = link.get('href')
            print('https://m1.megasliv.pro' + buf)


def get_pg_link():
    return input("First page link: ")


def get_page():
    return int(input("Page count: "))
