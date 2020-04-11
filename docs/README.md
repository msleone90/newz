# Newz
Local news straight to your terminal. 

Newz utilizes [wego](https://github.com/schachmat/wego) for weather visualizations, and Yahoo for financial and article data.

## Installation
`pip install newz`

## Dependencies
  * Python 2.7 or later
  * utf-8 terminal with 256 colors
  * An API key with [openweathermap](https://home.openweathermap.org/users/sign_up).

## Usage
To run **newz**, simply execute `python3 -m newz` or `newz` in your terminal/command line tool.

Newz uses the geocoder library to obtain your geolocation to provide the data. If you wish to obtain different location's news, just apply the `-c` or `--city` flags along with the name of the city.

## Contributing

1. Fork it (<https://github.com/msleone90/newz/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request