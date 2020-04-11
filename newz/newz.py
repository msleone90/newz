'''

Author: Michael Leone
git: github.com/msleone90
mail: msleone90@gmail.com
Requirements: requests, BeautifulSoup, selenium, geocoder, click, json, time

'''

from bs4 import BeautifulSoup
import click
import geocoder
import newz.weather as weather
import newz.articles as articles
from newz.newzconfig import *
from newz.finance import get_stock_data

def get_location():
      """ Uses geocoder library to retrieve city """
      geolocation = geocoder.ip('me')
      return geolocation.city

def format_weather_stock_section(forecast, stocks):
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

@click.command()
@click.option('-c', '--city', help='City to receive news', required=False)
def run(city):
      """ Get local news straight to the terminal """

      # Pull in city information if not specified
      if not city:
            city = get_location()

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
      response = weather.get_weather(city, weather_key)
      forecast = weather.format_data(response)

      # Grab stock data
      stock_data = get_stock_data()

      # Pull in top three local news stories from Yahoo
      stories = articles.get_articles(city)

      # Combines weather and stock sections
      ws_section = format_weather_stock_section(forecast, stock_data)

      # Display newz 
      print("""
-------------------------------------------------------------------------------------------------------------------------
| Local Weather                  | Finance                                                                              |
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
