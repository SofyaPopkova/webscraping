import requests
from bs4 import BeautifulSoup

KEYWORDS = {'дизайн', 'фото', 'web', 'Python'}
response = requests.get('https://habr.com/ru/all/')


def find_data():
    if not response.ok:
        raise ValueError('no response')
    else:
        text = response.text
        soup = BeautifulSoup(text, features='html.parser')
        articles = soup.find_all('article')
        print('Свежие статьи с ключевыми словами:')
        for article in articles:
            previews = {p.text for p in article.find_all('article', class_='post post_preview')}
            if KEYWORDS & previews:
                href = article.find('a', class_='post__title_link').attrs.get('href')
                data = article.find('span', class_='post__time').text
                title = article.find('a', class_='post__title_link').text
                print(f'<{data}> - <{title}> - <{href}')


find_data()
