import requests
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
    raw = requests.get(DAILY_FORECAST_ENDPOINT, params=params)
    pass
