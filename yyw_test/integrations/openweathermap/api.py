"""
this file is the only one that should be imported by external modules
the idea is to don't expose the structure of openweathermap
"""
from .utils import fetch_temperature_and_humidity_forecast_by_city_id


def search_city_by_name(query, results=10):
    """Take a query string and return a list of dictionaries of the cities that
    match that string.
    The returned list is formatted with a name and id

    Usage:
    cities = search_city_by_name('york')
    print(cities)
    [
        {
            'id': 12,
            'name': "York"
        },
        {
            'id': 1,
            'name': "New York"
        },
    ]
    """
    pass


def get_current_temperatures_and_humidity_by_city_id(city_id):
    """Return a dictionary of temperatures (in Celsius degrees) and humidity for the given city_id

    Usage
    temperature = get_current_temperatures_by_city_id(12)
    print(temperature)
    {
        'max': 26,
        'mix': 18,
        'average': 24,
        'humidity':
    }
    """
    raw = fetch_temperature_and_humidity_forecast_by_city_id(city_id)
    pass
