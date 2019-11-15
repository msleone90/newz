import requests
import selenium
from bs4 import BeautifulSoup

def formatLink(link):
    link = link.replace('/url?q=', "| ")
    link = link.split("&", 1)[0]

    return link

def formatArticleList(title, source, link):
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

def getArticles(city):
    article_list = []

    url = 'https://google.com/search?q=' + city + '&tbm=nws'
    source = requests.get(url, timeout=5)
    plain_text = source.text
    soup = BeautifulSoup(plain_text, "html5lib")

    articles = soup.findAll('div', {'class': 'g'})
    
    i = 0
    for item in articles:
        if i < 3:
            h3 = item.find('h3', attrs={'class':'r'})
            title = h3.find('a')
            source = item.find('div', attrs={'class':'slp'}).text.split("-", 1)[0].rstrip()
            link = formatLink(title['href'])

            article = formatArticleList(title.text, source, link)
            article_list.append(article)

            i += 1
        else:
            break
        
    return article_list