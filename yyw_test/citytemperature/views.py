from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from yyw_test.integrations.openweathermap.api import search_city_by_name, get_current_temperatures_and_humidity_by_city_id

from .serializers import CitySearchSerializer, ForecastSerializer


class CitySearchList(APIView):
    """Search throght the city in the database and return an id and the city name
    """
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        query = request.query_params.get('q')
        cities = search_city_by_name(query)
        serializer = CitySearchSerializer(cities, many=True)
        return Response(serializer.data)


class TodayForecastView(APIView):
    """Return the forcas for the current day given a city_id
    """
    permission_classes = (AllowAny,)

    def get(self, request, city_id, format=None):
        forecast = get_current_temperatures_and_humidity_by_city_id(city_id)
        serializer = ForecastSerializer(forecast)
        return Response(serializer.data)
