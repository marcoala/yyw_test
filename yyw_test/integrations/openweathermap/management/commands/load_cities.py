import ujson as json
import sys
import traceback

from django.utils import timezone
from django.db import transaction
from django.core.management.base import BaseCommand, CommandError

from yyw_test.integrations.openweathermap.models import City


# django will strip new lines split helptext in 80 char lines
HELP_TEXT = """
this command load the city in the database using a datafile downloaded from
openweathermap
"""

DATA_FILE = 'yyw_test/integrations/openweathermap/data/city.list.json'


class Command(BaseCommand):
    help = HELP_TEXT

    def handle(self, *args, **options):
        try:
            with transaction.atomic():
                self.stdout.write('Starting data loading')
                start_time = timezone.now()
                file_pointer = open(DATA_FILE, 'r')
                lines = file_pointer.readlines()
                counter = 0
                for line in lines:
                    city_data = json.loads(line)
                    city = City(
                        external_id=city_data['_id'],
                        name=city_data['name'],
                        country=city_data['country'])
                    city.save()
                    counter += 1
                    if counter == 1 or counter % 10000 == 0:
                        elasped_time = timezone.now() - start_time
                        print('Loaded {counter} cities in {elasped_time}'.format(counter=counter, elasped_time=elasped_time))
                elasped_time = timezone.now() - start_time
                self.stdout.write("Data loading completed in {elasped_time}, the database is now populated with default data.\n".format(elasped_time=elasped_time))
        except Exception as e:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            formatted_excption = traceback.format_exception(exc_type, exc_value, exc_traceback)
            for line in formatted_excption:
                self.stdout.write(line, ending='')
            raise CommandError("An exception occurred. All operations aborted, database rolled back.\n")
