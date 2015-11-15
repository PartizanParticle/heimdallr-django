import os
os.environ["DJANGO_SETTINGS_MODULE"]="heimdall.settings"

#sets up django shell environment
import django
django.setup()

#imports for adding database entries
from users.models import press_event
from tempinfo.models import weather

object_list = press_event.objects.all()
print('Deleting ' + str(len(object_list)) + ' press event database entries.')
for model in object_list:
    model.delete()

object_list = weather.objects.all()
print('Deleting ' + str(len(object_list)) + ' weather information database entries.')
for model in object_list:
    model.delete()

os.chdir(os.getcwd() + '/static/images/users')
image_list = os.listdir()
image_list.remove('defaults')

print('Removing ' + str(len(image_list)) + ' images.')
for image in image_list:
    os.remove(image)

print('Done!')
