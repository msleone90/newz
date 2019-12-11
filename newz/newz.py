'''

Author: Michael Leone 
git: github.com/msleone90
mail: msleone90@gmail.com
Requirements: requests, BeautifulSoup, selenium, geocoder

'''

from bs4 import BeautifulSoup
import geocoder
import newz.weather as weather
import requests
import json
import newz.articles as articles
from newz.newzconfig import * 
from newz.finance import getStockData

def getLocation():
      """ Uses geocoder library to retrieve city """
      g = geocoder.ip('me')
      return g.city

def formatWeatherStockSection(forecast, stocks):
      """ Combines weather and stock section into top half of newz """
      ws_section = ''

      forecast_line = forecast.split("\n")
      stock_line = stocks.split("\n")

      i = 0
      for i in range(len(stock_line)):
            if 6 > i > 0:
                  ws_section += "| " + forecast_line[i - 1] + stock_line[i] + "\n"
            elif i == 0 or i == 6:
                  ws_section += "|                                " + stock_line[i] + "\n"
            else:
                  ws_section += "|                                " + stock_line[i]
            i += 1

      return ws_section

def run():
      # Pull in city information
      city = getLocation()

      # Print header
      print("""  
       _   _  ______ __          __ ______
      | \ | ||  ____|\ \        / /|___  /
      |  \| || |__    \ \  /\  / /    / / 
      | . ` ||  __|    \ \/  \/ /    / /  
      | |\  || |____    \  /\  /    / /__ 
      |_| \_||______|    \/  \/    /_____|
      """)

      print("\n Today's Newz: " + city)

      # Retrieve local forecast and format it
      response = weather.getWeather(city, weather_key)
      forecast = weather.formatData(response)

      # Grab stock data
      stock_data = getStockData(stock_list)

      # Pull in top three local news stories from Yahoo
      stories = articles.getArticles(city)

      # Combines weather and stock sections
      ws_section = formatWeatherStockSection(forecast, stock_data)

      # Display newz 
      print("""
-------------------------------------------------------------------------------------------------------------------------
| Local Weather                  |  Finance                                                                             |
-------------------------------------------------------------------------------------------------------------------------
"""+ws_section+"""
-------------------------------------------------------------------------------------------------------------------------
| Headlines                                                                                                             |
-------------------------------------------------------------------------------------------------------------------------
"""+str(stories[0][0])+"""                                                                                          
|                                                                                                                       |
"""+str(stories[0][1])+"""                                                                                          
|                                                                                                                       |
|-----------------------------------------------------------------------------------------------------------------------|
"""+str(stories[1][0])+"""                                                                                          
|                                                                                                                       |
"""+str(stories[1][1])+"""                                                                                          
|                                                                                                                       |
|-----------------------------------------------------------------------------------------------------------------------|
"""+str(stories[2][0])+"""                                                                                          
|                                                                                                                       |
"""+str(stories[2][1])+"""                                                                                          
|                                                                                                                       |
|                                                                                                                       |
-------------------------------------------------------------------------------------------------------------------------
      """)