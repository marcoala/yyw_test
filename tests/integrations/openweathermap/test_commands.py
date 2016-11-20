from django.test import TestCase
from unittest.mock import mock_open, patch
from django.core.management import call_command, CommandError


from yyw_test.integrations.openweathermap.models import City

EXAMPLE_DATA = """{"_id":2643743,"name":"London","country":"GB","coord":{"lon":-0.12574,"lat":51.50853}}
{"_id":5128638,"name":"New York","country":"US","coord":{"lon":-75.499901,"lat":43.000351}}"""


BAD_EXAMPLE_DATA = "not json"


class TestCommands(TestCase):

    def test_load_city_basic_usage(self):
        mocked_open = mock_open(read_data=EXAMPLE_DATA)
        module_name = 'yyw_test.integrations.openweathermap.management.commands.load_cities'
        with patch('{}.open'.format(module_name), mocked_open, create=True):
            call_command('load_cities', interactive=False)
            london = City.objects.get(external_id=2643743)
            self.assertEqual(london.name, 'London')
            self.assertEqual(london.country, 'GB')

            new_york = City.objects.get(external_id=5128638)
            self.assertEqual(new_york.name, 'New York')
            self.assertEqual(new_york.country, 'US')

    def test_load_city_not_formatted_json(self):
        mocked_open = mock_open(read_data=BAD_EXAMPLE_DATA)
        module_name = 'yyw_test.integrations.openweathermap.management.commands.load_cities'
        with patch('{}.open'.format(module_name), mocked_open, create=True):
            with self.assertRaises(CommandError):
                call_command('load_cities', interactive=False)
