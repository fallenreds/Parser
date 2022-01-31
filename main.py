import func as fn
from bs4 import BeautifulSoup

url = 'https://m1.megasliv.pro/login/login'


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko)Chrome/92.0.4515.131 Safari/537.36 OPR/78.0.4093.186'
}

data = {
    'login': 'mops04@mail.ua',
    'password': 'mops2004',
    'remember': '1',
    '_xfRedirect': 'https://m1.megasliv.pro/',
    '_xfToken': '1641834074,103999586f3e03736bd81c8b02c58719'
}

try_session = fn.get_session(url, headers, data)
session = fn.final_session(try_session)

link = fn.get_pg_link()     #example    https://m1.megasliv.pro/forums/kitajskij-jazyk.79/
page_count = fn.get_page()
for i in range(1, page_count):
    if i == 1:
        pass
    else:
        link = link + str(i)
    site = session.get(link, headers=headers).text
    soup = BeautifulSoup(site, 'lxml')
    main_div = soup.find_all('div', class_='structItem-title')

    fn.print_name(main_div)
    name_list = fn.get_name(main_div)
    fn.get_href(main_div)