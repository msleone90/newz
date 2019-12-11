import datetime
import time
from yahoofinancials import YahooFinancials

def checkSectionLength(section):
    if len(section) > 28:
        diff = len(section) - 28
        section = section[:-(diff + 2)] + ".. "
    
    return section


def formatStockTitleSection(stock_dict):
    length = 28
    section_break = "| "
    stock_title_section = ""
    section_space = "|                            |                            |                            |\n"
    
    for key in stock_dict:
        stock_section = section_break + stock_dict[key]['name']

        stock_section = checkSectionLength(stock_section)

        i = 0
        for i in range(length - len(stock_section) + 1):
            stock_section += " "
            i += 1

        stock_title_section += stock_section

    stock_title_section += "|\n"
    stock_title_section += section_space

    return stock_title_section

def formatStockPriceSection(stock_dict):
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

def formatStockChangeSection(stock_dict):
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
        

def getStockData(stock_list):
    stock_dict = {}

    yahoo_financials = YahooFinancials(stock_list)
    stocks = yahoo_financials.get_stock_price_data()

    for item in stock_list:
        stock_dict[item.replace("^", '')] = {
            "name": stocks[item]['shortName'], 
            "price": stocks[item]['regularMarketPrice'], 
            "change-points": round(stocks[item]['regularMarketChange'], 2), 
            "change-percent": round(stocks[item]['regularMarketChangePercent'], 4)
        }

    stock_title_section = formatStockTitleSection(stock_dict)
    stock_price_section = formatStockPriceSection(stock_dict)
    stock_change_section = formatStockChangeSection(stock_dict)

    return stock_title_section + stock_price_section + stock_change_section