import datetime as dt
from flask import jsonify
import requests

BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'
API_KEY = open('api_key', 'r').read()


def kelvin_to_celsius_fahrenheit(kelvin):
    """
    > This function takes a temperature in Kelvin and returns the temperature in Celsius and Fahrenheit
    
    :param kelvin: The temperature in Kelvin
    :return: A tuple of two values, celsius and fahrenheit.
    """
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit


def mps_to_mph(mps):
    """
    > This function takes a speed in meters per second and returns the speed in miles per hour
    
    :param mps: meters per second
    :return: the value of mps * 2.237
    """
    return mps * 2.237
    

def get_response():
    """
    It will keep asking the user for a city until the user enters a valid city
    :return: A tuple containing the response and the city.
    """
    while True:
        city = input("Please enter a city.\n")

        url = BASE_URL + 'appid=' + API_KEY + '&q=' + city
        response =  requests.get(url).json()

        if 'main' in response:
            return response, response['name']
        else:
            raise "City not found. \n"


def main():

    response, city = get_response()

    temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(response['temp_kelvin'])
    feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(response['feels_like_kelvin'])

    data = {
        'main': response['main'],
        'city': city,
        'weather': response['weather'][0],
        'sys': response['sys'],
        'timezone': response['timezone'],
        'wind': response['wind'],
        'temp_celsius': temp_celsius,
        'temp_fahrenheit': temp_fahrenheit,
        'feels_like_celsius': feels_like_celsius,
        'feels_like_fahrenheit': feels_like_fahrenheit,
        'temp_kelvin': response['main']['temp'],
        'feels_like_kelvin': main['feels_like'],
        'wind_speed': response['wind']['speed'],
        'humidity': response['main']['humidity'],
        'description': response['weather']['description'],
        'sunrise_time': dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone']),
        'sunset_time': dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone']),
    }

    return jsonify(data)


if __name__ == "__main__":
    main()