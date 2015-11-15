from django.db import models
from django.utils import timezone

# Create your models here.
class press_event(models.Model):
	press_time = models.DateTimeField('Time of button push')
	height = models.FloatField(default=0)
	img_name = models.CharField(max_length=50,default='fail.jpg')

	known_person = models.BooleanField(default=False)

	def was_pressed_today(self):
		return (self.press_date.day==timezone.now().day and self.press_date.month==self.press_date.month)
	