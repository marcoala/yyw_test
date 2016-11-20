from django.test import TestCase
from yyw_test.integrations.openweathermap.models import City


class TestCity(TestCase):

    def test_string_convertions(self):
        city = City(external_id=123, name="London", country="GB")
        self.assertEqual(str(city), "London, GB")
