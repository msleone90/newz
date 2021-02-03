"""Module to build out weather section."""
import requests
from modules.forecast import format_weather
from modules.newzconfig import *

class ResponseNotFound(Exception):
    """Raised when a response is not returned from API call."""
    pass

def _check_rain(rain):
    """Checks if it is raining in searched city."""
    if "rain" not in rain:
        return ""
    return rain

def get_weather(city, key):
    """Pulls response data from openweathermap API."""
    url = WEATHER_API_URL + '/data/2.5/weather?q='
    try:
        url += city + '&units=Imperial&appid=' + key
        response = requests.get(url)
    except ResponseNotFound:
        print("Unable to return a response")
    return response

def format_data(response):
    """Formats response data into weather dictionary."""
    forecast = {}
    response = response.json()

    # Build forecast widget data structure
    forecast = {
        "currentTemp": str(round(response['main']['temp']))+' F',
        "weather": response['weather'][0]['main'],
        "location": response['name'] + ", + " + response['sys']['country'],
        "wind": str(response['wind']['speed']) + " mph",
        "code": str(response['weather'][0]['id']),
        "humidity": str(round(response['main']['humidity'])) + "% HUM",
        "rain": _check_rain(response)
    }

    forecast = format_weather(forecast)
    return forecast
