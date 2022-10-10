import datetime as dt
import requests

BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'
API_KEY = open('api_key', 'r').read()
CITY = "Ontario"


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

def main():

    # This is creating a URL that will be used to make a request to the OpenWeatherMap API. The
    url = BASE_URL + 'appid=' + API_KEY + '&q=' + CITY
    response = requests.get(url).json()

    # unpack the response
    main = response['main']
    weather = response['weather'][0]
    sys = response['sys']
    timezone = response['timezone']
    wind = response['wind']

    temp_kelvin = main['temp']
    temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
    feels_like_kelvin = main['feels_like']
    feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)
    wind_speed = wind['speed']
    humidity = main['humidity']
    description = weather['description']
    sunrise_time = dt.datetime.utcfromtimestamp(sys['sunrise'] + timezone)
    sunset_time = dt.datetime.utcfromtimestamp(sys['sunset'] + timezone)

    print(f"Temperature in {CITY}: {temp_celsius:.0f}C or {temp_fahrenheit:.0f}F")
    print(f"Temperature in {CITY} feels like: {feels_like_celsius:.0f}C or {feels_like_fahrenheit:.0f}F")
    print(f"Humidity in {CITY}: {humidity}%")
    print(f"Wind Speed in {CITY}: {mps_to_mph(wind_speed):.1f}mph")
    print(f"General Weather in {CITY}: {description}")
    print(f"Sun Rises in {CITY} at {sunrise_time} local time.")
    print(f"Sun Sets in {CITY} at {sunset_time} local time.")

if __name__ == "__main__":
    main()