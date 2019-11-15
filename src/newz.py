'''

Author: Michael Leone 
git: github.com/msleone90
mail: msleone90@gmail.com
Requirements: requests, BeautifulSoup, selenium

'''

from bs4 import BeautifulSoup
import weather
import requests
import json
import articles
from newzconfig import * 
from finance import getStockData

response = weather.getWeather(city, weather_key)
forecast = weather.formatData(response)
stock_data = getStockData(stock_list)

response1 = articles.getArticles(city)

print("""  
  _   _  ______ __          __ ______
 | \ | ||  ____|\ \        / /|___  /
 |  \| || |__    \ \  /\  / /    / / 
 | . ` ||  __|    \ \/  \/ /    / /  
 | |\  || |____    \  /\  /    / /__ 
 |_| \_||______|    \/  \/    /_____|
 """)

print("\n Today's Newz: " + forecast['location'])
print("""
┌────────────────────────────────┬──────────────────────────────────────────────────────────────────────────────────────┐
| Local Weather                  |  Finance                                                                             |
|────────────────────────────────|──────────────────────────────────────────────────────────────────────────────────────|
"""+stock_data+"""
|───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────|
| Headlines                                                                                                             |
|───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────|
"""+str(response1[0][0])+"""                                                                                          
|                                                                                                                       |
"""+str(response1[0][1])+"""                                                                                          
|                                                                                                                       |
|-----------------------------------------------------------------------------------------------------------------------|
"""+str(response1[1][0])+"""                                                                                          
|                                                                                                                       |
"""+str(response1[1][1])+"""                                                                                          
|                                                                                                                       |
|-----------------------------------------------------------------------------------------------------------------------|
"""+str(response1[2][0])+"""                                                                                          
|                                                                                                                       |
"""+str(response1[2][1])+"""                                                                                          
|                                                                                                                       |
|                                                                                                                       |
└───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
""")