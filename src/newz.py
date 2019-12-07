'''

Author: Michael Leone 
git: github.com/msleone90
mail: msleone90@gmail.com
Requirements: requests, BeautifulSoup, selenium

'''

from bs4 import BeautifulSoup
import geocoder
import weather
import requests
import json
import articles
from newzconfig import * 
from finance import getStockData

def getLocation():
      g = geocoder.ip('me')
      return g.city

def formatWeatherStockSection(forecast, stocks):
      ws_section = ''

      forecast_line = forecast.split("\n")
      stock_line = stocks.split("\n")

      ws_section += "|                                " + stock_line[0] + "\n"
      ws_section += "| " + forecast_line[0] + stock_line[1] + "\n"
      ws_section += "| " + forecast_line[1] + stock_line[2] + "\n"
      ws_section += "| " + forecast_line[2] + stock_line[3] + "\n"
      ws_section += "| " + forecast_line[3] + stock_line[4] + "\n"
      ws_section += "| " + forecast_line[4] + stock_line[5] + "\n"
      ws_section += "|                                " + stock_line[6] + "\n"
      ws_section += "|                                " + stock_line[7]


      return ws_section

city = getLocation()

print("""  
  _   _  ______ __          __ ______
 | \ | ||  ____|\ \        / /|___  /
 |  \| || |__    \ \  /\  / /    / / 
 | . ` ||  __|    \ \/  \/ /    / /  
 | |\  || |____    \  /\  /    / /__ 
 |_| \_||______|    \/  \/    /_____|
 """)

print("\n Today's Newz: " + city)

response = weather.getWeather(city, weather_key)
forecast = weather.formatData(response)

stock_data = getStockData(stock_list)

articles = articles.getArticles(city)

ws_section = formatWeatherStockSection(forecast, stock_data)

print("""
-------------------------------------------------------------------------------------------------------------------------
| Local Weather                  |  Finance                                                                             |
-------------------------------------------------------------------------------------------------------------------------
"""+ws_section+"""
-------------------------------------------------------------------------------------------------------------------------
| Headlines                                                                                                             |
-------------------------------------------------------------------------------------------------------------------------
"""+str(articles[0][0])+"""                                                                                          
|                                                                                                                       |
"""+str(articles[0][1])+"""                                                                                          
|                                                                                                                       |
|-----------------------------------------------------------------------------------------------------------------------|
"""+str(articles[1][0])+"""                                                                                          
|                                                                                                                       |
"""+str(articles[1][1])+"""                                                                                          
|                                                                                                                       |
|-----------------------------------------------------------------------------------------------------------------------|
"""+str(articles[2][0])+"""                                                                                          
|                                                                                                                       |
"""+str(articles[2][1])+"""                                                                                          
|                                                                                                                       |
|                                                                                                                       |
-------------------------------------------------------------------------------------------------------------------------
""")
                                