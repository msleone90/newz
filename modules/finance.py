"""Module to build out finance section."""
import bs4
from bs4 import BeautifulSoup
from modules import newzconfig
import requests

def _check_section_length(section):
    """Determines length of stock section."""
    if len(section) > 28:
        diff = len(section) - 28
        section = section[:-(diff + 2)] + ".. "

    return section


def _format_stock_title_section(stock_dict):
    """Formats individual stock section header."""
    length = 28
    section_break = "| "
    stock_title_section = ""
    section_space = "|                            |                            |                            |\n"

    for key in stock_dict:
        stock_section = section_break + stock_dict[key]['name']

        stock_section = _check_section_length(stock_section)

        i = 0
        for i in range(length - len(stock_section) + 1):
            stock_section += " "
            i += 1

        stock_title_section += stock_section

    stock_title_section += "|\n"
    stock_title_section += section_space

    return stock_title_section

def _format_stock_price_section(stock_dict):
    """Formats individual stock section price."""
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

def _format_stock_change_section(stock_dict):
    """Formats individual stock section change %."""
    length = 43
    section_break = "| "
    stock_title_section = "| Change(%):                 | Change(%):                 | Change(%):                 |\n"
    section_space = "|                            |                            |                            |"

    for key in stock_dict:
        if "-" in str(stock_dict[key]['change-percent']):
            stock_section = section_break + "(\033[38;5;196m" + str(stock_dict[key]['change-percent']) + "\033[0m)"
        else:
            stock_section = section_break + "(\033[38;5;118m" + str(stock_dict[key]['change-percent']) + "\033[0m)"

        i = 0
        for i in range(length - len(stock_section) + 1):
            stock_section += " "
            i += 1

        stock_title_section += stock_section

    stock_title_section += "|\n"
    stock_title_section += section_space

    return stock_title_section


def get_stock_data():
    """Function to obtain stock data from Yahoo."""
    stock_item = {}
    stock_dict = {}

    stock_request = requests.get(YAHOO_FINANCE_URL)
    soup = bs4.BeautifulSoup(stock_request.text, 'html5lib')
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

    stock_title_section = _format_stock_title_section(stock_dict)
    stock_price_section = _format_stock_price_section(stock_dict)
    stock_change_section = _format_stock_change_section(stock_dict)

    return stock_title_section + stock_price_section + stock_change_section
