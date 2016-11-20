from django.db import models

# Create your models here.


class City(models.Model):
    external_id = models.PositiveIntegerField(null=False, blank=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    # probably django-country is a better option for this field
    country = models.CharField(max_length=2, null=False, blank=False)

    def __str__(self):
        return '{name}, {country}'.format(name=self.name, country=self.country)
