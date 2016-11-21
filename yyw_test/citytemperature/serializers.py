from rest_framework import serializers


class CitySearchSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    name = serializers.CharField(max_length=255, required=True)


class ForecastSerializer(serializers.Serializer):
    max = serializers.FloatField(required=True)
    min = serializers.FloatField(required=True)
    average = serializers.FloatField(required=True)
    humidity = serializers.FloatField(required=True)
