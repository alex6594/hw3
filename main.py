import bs4
import requests

base_url = 'https://habr.com'
HEADERS = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,'
                     '*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
           'Accept-Encoding': 'gzip, deflate, br',
           'Accept-Language': 'ru,en;q=0.9',
           'Cache-Control': 'max-age=0',
           'Connection': 'keep-alive',
           'Cookie': '_ym_d=1628840683; _ym_uid=1628840683355101683; _ga=GA1.2.137596937.1628841988; fl=ru; hl=ru; '
                     'feature_streaming_comments=true; _gid=GA1.2.1021543475.1641571984; '
                     'habr_web_home=ARTICLES_LIST_ALL; _ym_isad=1; visited_articles=599735:203282; '
                     'SLG_GWPT_Show_Hide_tmp=1; SLG_wptGlobTipTmp=1',
           'Host': 'habr.com',
           'Referer': 'https://github.com/netology-code/py-homeworks-advanced/tree/master/6.Web-scrapping',
           'sec-ch-ua': '"Chromium";v="94", "Yandex";v="21", ";Not A Brand";v="99"',
           'sec-ch-ua-mobile': '?0',
           'sec-ch-ua-platform': '"Windows"',
           'Sec-Fetch-Dest': 'document',
           'Sec-Fetch-Mode': 'navigate',
           'Sec-Fetch-Site': 'same-origin',
           'Sec-Fetch-User': '?1',
           'Upgrade-Insecure-Requests': '1',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/94.0.4606.85 YaBrowser/21.11.4.727 Yowser/2.5 Safari/537.36'}
url = base_url + '/ru/all/'


def keywords():
    keywords_find = []
    while True:
        keyword_find = input('Введите ключевое слово для поиска в тексте или exit для выхода: ')
        if keyword_find == 'exit':
            return keywords_find
        else:
            keywords_find.append(keyword_find)


response = requests.get(base_url, headers=HEADERS)
text = response.text
soup = bs4.BeautifulSoup(text, features='html.parser')
hub_text = soup.find_all('article')
time = soup.find_all('time')
hub_name = soup.find_all()
keywords = keywords()
for hub_1 in hub_text:
    hubs = hub_1.find_all(class_="article-formatted-body article-formatted-body article-formatted-body_version-2")
    hubs = [hub.text.strip() for hub in hubs]
    for hub in hubs:
        for keyword in keywords:
            if keyword in hub:
                date_time = hub_1.find(class_='tm-article-snippet__datetime-published')
                hub_head = hub_1.find(class_="tm-article-snippet__title-link")
                href = hub_1.find(class_="tm-article-snippet__readmore").attrs['href']
                print(f'{date_time.text} - {hub_head.text} - {base_url + href}')
