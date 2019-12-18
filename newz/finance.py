import bs4
import requests
from bs4 import BeautifulSoup

def _checkSectionLength(section):
    if len(section) > 28:
        diff = len(section) - 28
        section = section[:-(diff + 2)] + ".. "
    
    return section


def _formatStockTitleSection(stock_dict):
    length = 28
    section_break = "| "
    stock_title_section = ""
    section_space = "|                            |                            |                            |\n"
    
    for key in stock_dict:
        stock_section = section_break + stock_dict[key]['name']

        stock_section = _checkSectionLength(stock_section)

        i = 0
        for i in range(length - len(stock_section) + 1):
            stock_section += " "
            i += 1

        stock_title_section += stock_section

    stock_title_section += "|\n"
    stock_title_section += section_space

    return stock_title_section

def _formatStockPriceSection(stock_dict):
    length = 28
    section_break = "| "
    stock_price_section = "| Price:                     | Price:                     | Price:                     |\n"
    section_space = "|                            |                            |                            |\n"
    
    for key in stock_dict:
        stock_section = section_break + str(stock_dict[key]['price'])

        i = 0
        if len(stock_section) < length:
            for i in range(length - len(stock_section) + 1):
                stock_section += " "
                i += 1

        stock_price_section += stock_section

    stock_price_section += "|\n"
    stock_price_section += section_space

    return stock_price_section

def _formatStockChangeSection(stock_dict):
    length = 28
    section_break = "| "
    stock_title_section = "| Change(%):                 | Change(%):                 | Change(%):                 |\n"
    section_space = "|                            |                            |                            |"
    
    for key in stock_dict:
        stock_section = section_break + str(stock_dict[key]['change-points']) + "(" + str(stock_dict[key]['change-percent']) + ")"

        i = 0
        for i in range(length - len(stock_section) + 1):
            stock_section += " "
            i += 1

        stock_title_section += stock_section

    stock_title_section += "|\n"
    stock_title_section += section_space

    return stock_title_section
        

def getStockData():
    stock_item = {}
    stock_dict = {}

    r = requests.get('https://finance.yahoo.com/')
    soup = bs4.BeautifulSoup(r.text, 'html5lib')
    stocks = soup.find_all('li', {'class': 'Bxz(bb)'})

    i = 0
    for stock in stocks:
        if i < 3:
            stock_item['name'] = stock.find('a')['title']
            spans = stock.find_all('span')
            
            j = 0
            for span in spans:
                if j < 1:
                    stock_item['price'] = span.text
                else:
                    stock_item['change-points'] = span.text
                    stock_item['change-percent'] = span.text
                j += 1
        else:
            break
            
        stock_dict[stock_item['name']] = {
            "name": stock_item['name'], 
            "price": stock_item['price'], 
            "change-points": stock_item['change-points'], 
            "change-percent": stock_item['change-percent']
        }

        i += 1

    stock_title_section = _formatStockTitleSection(stock_dict)
    stock_price_section = _formatStockPriceSection(stock_dict)
    stock_change_section = _formatStockChangeSection(stock_dict)

    return stock_title_section + stock_price_section + stock_change_section
