import requests
import selenium
import json
from bs4 import BeautifulSoup

def __formatSpacing(details):
    length = 19
    spaces = ''

    i = 0
    if len(details) < length:
        for i in range(length - len(details) - 1):
            spaces += " "
    
    return spaces

def __formatRain(rain):
	if not rain:
			return "0.0 in."
	else:
			return str(rain['rain']['1h']) + " in."

def __buildWeatherSection(code, forecast):
    weather_section =''

    weather_dict = {
        'Unknown': (
 			"    .-.      \n" +
 			"     __)     \n" +
 			"    (        \n" +
 			"     `-'     \n" +
 			"      •      \n" 
 		),
 		'Cloudy': (
            "             \n" +
            "\033[38;5;250m     .--.    \033[0m\n" +
            "\033[38;5;250m  .-(    ).  \033[0m\n" +
            "\033[38;5;250m (___.__)__) \033[0m\n" +
            "             \n"
        ),
		'Fog': (
			"             \n" +
			"\033[38;5;251m _ - _ - _ - \033[0m\n" +
			"\033[38;5;251m  _ - _ - _  \033[0m\n" +
			"\033[38;5;251m _ - _ - _ - \033[0m\n" +
			"             \n"
		),
		'HeavyRain': (
			"\033[38;5;240;1m     .-.     \033[0m\n" +
			"\033[38;5;240;1m    (   ).   \033[0m\n" +
			"\033[38;5;240;1m   (___(__)  \033[0m\n" +
			"\033[38;5;21;1m  ‚'‚'‚'‚'   \033[0m\n" +
			"\033[38;5;21;1m  ‚'‚'‚','   \033[0m\n"
		),
		'HeavyShowers': (
			"\033[38;5;226m _`/\"\"\033[38;5;240;1m.-.    \033[0m\n" +
			"\033[38;5;226m  ,\\_\033[38;5;240;1m(   ).  \033[0m\n" +
			"\033[38;5;226m   /\033[38;5;240;1m(___(__) \033[0m\n" +
			"\033[38;5;21;1m   ‚'‚'‚'‚'  \033[0m\n" +
			"\033[38;5;21;1m   ‚'‚'‚'‚'  \033[0m\n"
		),
		'HeavySnow': (
			"\033[38;5;240;1m     .-.     \033[0m\n" +
			"\033[38;5;240;1m    (   ).   \033[0m\n" +
			"\033[38;5;240;1m   (___(__)  \033[0m\n" +
			"\033[38;5;255;1m   * * * *   \033[0m\n" +
			"\033[38;5;255;1m  * * * *    \033[0m\n"
		),
		'HeavySnowShowers': (
			"\033[38;5;226m _`/\"\"\033[38;5;240;1m.-.    \033[0m\n" +
			"\033[38;5;226m  ,\\_\033[38;5;240;1m(   ).  \033[0m\n" +
			"\033[38;5;226m   /\033[38;5;240;1m(___(__) \033[0m\n" +
			"\033[38;5;255;1m    * * * *  \033[0m\n" +
			"\033[38;5;255;1m   * * * *   \033[0m\n"
		),
		'LightRain': (
			"\033[38;5;250m     .-.     \033[0m\n" +
			"\033[38;5;250m    (   ).   \033[0m\n" +
			"\033[38;5;250m   (___(__)  \033[0m\n" +
			"\033[38;5;111m    ' ' ' '  \033[0m\n" +
			"\033[38;5;111m   ' ' ' '   \033[0m\n"
		),
		'LightShowers': (
			"\033[38;5;226m _`/\"\"\033[38;5;250m.-.    \033[0m\n" +
			"\033[38;5;226m  ,\\_\033[38;5;250m(   ).  \033[0m\n" +
			"\033[38;5;226m   /\033[38;5;250m(___(__) \033[0m\n" +
			"\033[38;5;111m     ' ' ' ' \033[0m\n" +
			"\033[38;5;111m    ' ' ' '  \033[0m\n"
		),
		'LightSleet': (
			"\033[38;5;250m     .-.     \033[0m\n" +
			"\033[38;5;250m    (   ).   \033[0m\n" +
			"\033[38;5;250m   (___(__)  \033[0m\n" +
			"\033[38;5;111m    ' \033[38;5;255m*\033[38;5;111m ' \033[38;5;255m*  \033[0m\n" +
			"\033[38;5;255m   *\033[38;5;111m ' \033[38;5;255m*\033[38;5;111m '   \033[0m\n"
		),
		'LightSleetShowers': (
			"\033[38;5;226m _`/\"\"\033[38;5;250m.-.    \033[0m\n" +
			"\033[38;5;226m  ,\\_\033[38;5;250m(   ).  \033[0m\n" +
			"\033[38;5;226m   /\033[38;5;250m(___(__) \033[0m\n" +
			"\033[38;5;111m     ' \033[38;5;255m*\033[38;5;111m ' \033[38;5;255m* \033[0m\n" +
			"\033[38;5;255m    *\033[38;5;111m ' \033[38;5;255m*\033[38;5;111m '  \033[0m\n"
		),
		'LightSnow': (
			"\033[38;5;250m     .-.     \033[0m\n" +
			"\033[38;5;250m    (   ).   \033[0m\n" +
			"\033[38;5;250m   (___(__)  \033[0m\n" +
			"\033[38;5;255m    *  *  *  \033[0m\n" +
			"\033[38;5;255m   *  *  *   \033[0m\n"
		),
		'LightSnowShowers': (
			"\033[38;5;226m _`/\"\"\033[38;5;250m.-.    \033[0m\n" +
			"\033[38;5;226m  ,\\_\033[38;5;250m(   ).  \033[0m\n" +
			"\033[38;5;226m   /\033[38;5;250m(___(__) \033[0m\n" +
			"\033[38;5;255m     *  *  * \033[0m\n" +
			"\033[38;5;255m    *  *  *  \033[0m\n"
		),
		'PartlyCloudy': (
			"\033[38;5;226m   \\  /\033[0m      \n" +
			"\033[38;5;226m _ /\"\"\033[38;5;250m.-.    \033[0m\n" +
			"\033[38;5;226m   \\_\033[38;5;250m(   ).  \033[0m\n" +
			"\033[38;5;226m   /\033[38;5;250m(___(__) \033[0m\n"
			"             \n"
		),
		'Sunny': (
			"\033[38;5;226m    \\   /    \033[0m\n" +
			"\033[38;5;226m     .-.     \033[0m\n" +
			"\033[38;5;226m  - (   ) -  \033[0m\n" +
			"\033[38;5;226m     `-'     \033[0m\n" +
			"\033[38;5;226m    /   \\    \033[0m\n"
		),
		'ThunderyHeavyRain': (
			"\033[38;5;240;1m     .-.     \033[0m\n" +
			"\033[38;5;240;1m    (   ).   \033[0m\n" +
			"\033[38;5;240;1m   (___(__)  \033[0m\n" +
			"\033[38;5;21;1m  ‚'\033[38;5;228;5m⚡\033[38;5;21;25m'‚\033[38;5;228;5m⚡\033[38;5;21;25m‚'   \033[0m\n" +
			"\033[38;5;21;1m  ‚'‚'\033[38;5;228;5m⚡\033[38;5;21;25m'‚'   \033[0m\n"
		),
		'ThunderyShowers': (
			"\033[38;5;226m _`/\"\"\033[38;5;250m.-.    \033[0m\n" +
			"\033[38;5;226m  ,\\_\033[38;5;250m(   ).  \033[0m\n" +
			"\033[38;5;226m   /\033[38;5;250m(___(__) \033[0m\n" +
			"\033[38;5;228;5m    ⚡\033[38;5;111;25m' '\033[38;5;228;5m⚡\033[38;5;111;25m' ' \033[0m\n" +
			"\033[38;5;111m    ' ' ' '  \033[0m\n"
		),
		'ThunderySnowShowers': (
			"\033[38;5;226m _`/\"\"\033[38;5;250m.-.    \033[0m\n" +
			"\033[38;5;226m  ,\\_\033[38;5;250m(   ).  \033[0m\n" +
			"\033[38;5;226m   /\033[38;5;250m(___(__) \033[0m\n" +
			"\033[38;5;255m     *\033[38;5;228;5m⚡\033[38;5;255;25m *\033[38;5;228;5m⚡\033[38;5;255;25m * \033[0m\n" +
			"\033[38;5;255m    *  *  *  \033[0m\n"
		),
		'VeryCloudy': (
			"             \n" +
			"\033[38;5;240;1m     .--.    \033[0m\n" +
			"\033[38;5;240;1m  .-(    ).  \033[0m\n" +
			"\033[38;5;240;1m (___.__)__) \033[0m\n" +
			"             \n"
		)
    }

    weather_list = weather_dict[code].split('\n')
    rain = __formatRain(forecast['rain'])

    weather_section += weather_list[0] + forecast['weather'] + __formatSpacing(forecast['weather']) + '\n'
    weather_section += weather_list[1] + forecast['currentTemp'] + __formatSpacing(forecast['currentTemp']) + '\n'
    weather_section += weather_list[2] + forecast['wind'] + __formatSpacing(forecast['wind']) + '\n'
    weather_section += weather_list[3] + forecast['humidity'] + __formatSpacing(forecast['humidity']) + '\n'
    weather_section += weather_list[4] + rain + __formatSpacing(rain) + '\n'

    return weather_section

def formatWeather(forecast):
    weather_codes = {
        '200': 'ThunderyShowers',
        '201': 'ThunderyShowers',
        '210': 'ThunderyShowers',
        '230': 'ThunderyShowers',
        '231': 'ThunderyShowers',
        '202': 'ThunderyHeavyRain',
        '211': 'ThunderyHeavyRain',
        '212': 'ThunderyHeavyRain',
        '221': 'ThunderyHeavyRain',
        '232': 'ThunderyHeavyRain',
        '300': 'LightRain',
        '301': 'LightRain',
        '310': 'LightRain',
        '311': 'LightRain',
        '313': 'LightRain',
        '321': 'LightRain',
        '302': 'HeavyRain',
        '312': 'HeavyRain',
        '314': 'HeavyRain',
        '500': 'LightShowers',
        '501': 'LightShowers',
        '502': 'HeavyShowers',
        '503': 'HeavyShowers',
        '504': 'HeavyShowers',
        '511': 'LightSleet',
        '520': 'LightShowers',
        '521': 'LightShowers',
        '522': 'HeavyShowers',
        '531': 'HeavyShowers',
        '600': 'LightSnow',
        '601': 'LightSnow',
        '602': 'HeavySnow',
        '611': 'LightSleet',
        '612': 'LightSleetShowers',
        '615': 'LightSleet',
        '616': 'LightSleet',
        '620': 'LightSnowShowers',
        '621': 'LightSnowShowers',
        '622': 'HeavySnowShowers',
        '701': 'Fog',
        '711': 'Fog',
        '721': 'Fog',
        '741': 'Fog',
        '731': 'Unknown', # sand', dust whirls
        '751': 'Unknown', # sand
        '761': 'Unknown', # dust
        '762': 'Unknown', # volcanic ash
        '771': 'Unknown', # squalls
        '781': 'Unknown', # tornado
        '800': 'Sunny',
        '801': 'PartlyCloudy',
        '802': 'Cloudy',
        '803': 'VeryCloudy',
        '804': 'VeryCloudy',
        '900': 'Unknown', # tornado
        '901': 'Unknown', # tropical storm
        '902': 'Unknown', # hurricane
        '903': 'Unknown', # cold
        '904': 'Unknown', # hot
        '905': 'Unknown', # windy
        '906': 'Unknown', # hail
        '951': 'Unknown', # calm
        '952': 'Unknown', # light breeze
        '953': 'Unknown', # gentle breeze
        '954': 'Unknown', # moderate breeze
        '955': 'Unknown', # fresh breeze
        '956': 'Unknown', # strong breeze
        '957': 'Unknown', # high wind near gale
        '958': 'Unknown', # gale
        '959': 'Unknown', # severe gale
        '960': 'Unknown', # storm
        '961': 'Unknown', # violent storm
        '962': 'Unknown' # hurricane
    }

    forecast = __buildWeatherSection(weather_codes[forecast['code']], forecast)

    return forecast