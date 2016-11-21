import requests
from datetime import date
from .settings import API_KEY, DAILY_FORECAST_ENDPOINT


def fetch_temperature_and_humidity_forecast_by_city_id(city_id):
    """Connect to the remote server and collect the temperature data for the next 16 days
    return a list of 16 dictionaries, with date, and the following temperatures:
    day, min, max , night, eve, morn
    and the humidity

    Usage:
    temperatures_forecast = fetch_temperature_forecast_by_city_id(42)
    print(len(temperatures_forecast))
        16
    print(temperatures_forecast)
    [
        {
            'date': date(1, 6, 2016),
            'day': 24,
            'min': 29,
            'max': 25,
            'night': 18,
            'eve': 19,
            'morn': 20,
            'humidity': 98
        },
        ...
    ]
    """
    params = {
        'id': city_id,
        'APPID': API_KEY,
        'cnt': 16,
        'units': 'metric'
    }
    response = requests.get(DAILY_FORECAST_ENDPOINT, params=params)
    # at this pint I should check the http repsonse (code is 200, that the response it not empty
    raw = response.json()
    raw_daily_forecast = raw['list']
    daily_forecast = []
    for row in raw_daily_forecast:
        day = {
            'date': date.fromtimestamp(row['dt']),
            'day': row['temp']['day'],
            'min': row['temp']['min'],
            'max': row['temp']['max'],
            'night': row['temp']['night'],
            'eve': row['temp']['eve'],
            'morn': row['temp']['morn'],
            'humidity': row['humidity']
        }
        daily_forecast.append(day)
    return daily_forecast
