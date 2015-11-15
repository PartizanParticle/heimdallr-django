from django.db import models

# Create your models here.
class weather(models.Model):
    weather_time = models.DateTimeField('Timestamp of weather info')
    temperature = models.FloatField(default=0)
    humidity = models.FloatField(default=0)
