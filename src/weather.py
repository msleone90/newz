import requests
import selenium
import json
from bs4 import BeautifulSoup

def getWeather(city, key):
    try:
        url = 'http://api.openweathermap.org/data/2.5/weather?q=Atlanta&units=Imperial&appid=' + key
        response = requests.get(url)
    except:
        print("Unable to return a response")
    return response

def formatData(response):
    forecast = {}
    response = response.json()

    # Build forecast widget data structure
    forecast = {
        "currentTemp": str(round(response['main']['temp']))+'°',
        "weather": response['weather'][0]['main'],
        "location": response['name'] + ", " + response['sys']['country'],
        "wind": str(response['wind']['speed']) + " mph"
    }

    return forecast 