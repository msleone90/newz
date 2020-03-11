"""Module to build out articles section."""
import requests
from bs4 import BeautifulSoup

def format_article_list(title, source, link):
    """Prepares articles for section."""
    i = 0
    length = 120
    space = " "
    article_headline = "| " + title + " - " + source

    if len(article_headline) < length:
        for i in range(length - len(article_headline)):
            article_headline += space
        article_headline += "|"

    if len(link) < length:
        for i in range(length - len(link)):
            link += space
        link += "|"

    return [article_headline, link]

def get_articles(city):
    """Grabs top three articles from Yahoo."""
    article_list = []

    url = 'https://news.search.yahoo.com/search;?p=' + city
    source = requests.get(url, timeout=5)
    plain_text = source.text
    soup = BeautifulSoup(plain_text, "html5lib")

    articles = soup.findAll('div', {'class': 'NewsArticle'})

    i = 0
    for item in articles:
        if i < 3:
            title = item.find('a', attrs={'class':'thmb'})['title']
            source = item.find('span', attrs={'class':'mr-5'}).text
            header4 = item.find('h4', attrs={'class':'fz-16'})
            link = header4.find('a')['href']

            article = format_article_list(title, source, "| " + link)
            article_list.append(article)

            i += 1
        else:
            break

    return article_list
