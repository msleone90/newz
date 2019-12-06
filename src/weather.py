import requests
import selenium
import json
from bs4 import BeautifulSoup
from forecast import formatWeather

def __checkRain(rain):
    if "rain" not in rain:
        return ""
    else:
        return rain

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
        "currentTemp": str(round(response['main']['temp']))+' °F',
        "weather": response['weather'][0]['main'],
        "location": response['name'] + ", + " + response['sys']['country'],
        "wind": str(response['wind']['speed']) + " mph",
        "code": str(response['weather'][0]['id']),
        "humidity": str(round(response['main']['humidity'])) + "% HUM",
        "rain": __checkRain(response)
    }

    forecast = formatWeather(forecast)
    return forecast

