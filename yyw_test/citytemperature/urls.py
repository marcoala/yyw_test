from django.conf.urls import url
from . views import CitySearchList, TodayForecastView

urlpatterns = [
    url(
        regex=r'^v1\.0/city/$',
        view=CitySearchList.as_view(),
        name='city_search'
    ),
    url(
        regex=r'^v1\.0/forecast/(?P<city_id>\w+)/$',
        view=TodayForecastView.as_view(),
        name='forecast'
    ),
]
