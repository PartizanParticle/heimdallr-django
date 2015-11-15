import vlc

#initialising VLC instance and beginning player
instance = vlc.Instance()
media = vlc.libvlc_media_new_location(instance, b"dshow://")
player = vlc.libvlc_media_player_new_from_media(media)
response = vlc.libvlc_media_player_play(player)
if response is not 0:
	print("Camera interface could not be initialised \n Continuing routine using default image.\n")
	if media is None:
		print('Media object not initialised correctly.\n')
	elif media is not None and player is None:
		print('Media onject initialised, but player failed to create.\n')

#Configuring where django looks for settings
import os
os.environ["DJANGO_SETTINGS_MODULE"]="heimdall.settings"

#sets up django shell environment
import django
django.setup()

#imports for adding database entries
from users.models import press_event
from tempinfo.models import weather
from django.utils import timezone

#TESTING using serial from arduino
import serial
import time
import random
from dist import *

#Change port here to arduino serial port
ser = serial.Serial(
	port='COM3',\
	baudrate=9600,\
	bytesize=serial.EIGHTBITS,\
	timeout=3)
time.sleep(1)

print("connected to arduino on: "+ser.portstr)

height_for_cal = 300

#Code for checking if file exists
os.chdir("static")
file_list = os.listdir()
if "height.txt" in file_list:
	testfile=open("height.txt", "r")
	for line in testfile:
		height_for_cal=float(line)
	testfile.close()
os.chdir("..")

image_count = len(press_event.objects.all())
os.chdir(os.getcwd() + '/static/images/users')


#Main loop which handles serial information
while True:
	serialString=str(ser.readline())
	serialString=serialString.strip("b'")
	serialString=serialString.strip("\\r\\n")
	serialString=serialString.split(',')
	event_type = serialString[0]

	if(event_type == "pressed"):

		vlc.libvlc_video_take_snapshot(player, 0, os.getcwdb(), 0, 0)

		#Cheeky hack to get a list of images, and take the name of the one which has just been taken
		image_list = os.listdir()
		image_list.remove('defaults')
		image_name = image_list[image_count]

		image_count+=1

		#Calculate height from temp and humidity using func

		time_now=timezone.now()

		duration=float(serialString[1]) #looking at serial info
		humid=float(serialString[2])
		temper=float(serialString[3])

		#distance is the function using the lookup table
		hgt=round((height_for_cal-(100*distance(temper, humid, duration))), 2)

		#Constructing a new event with all information
		event=press_event(press_time=time_now,height=hgt,img_name=image_name)

		#reporting it's been generated, then saving it to the database
		print("generated event at: " + str(time_now.hour)+":"+str(time_now.minute) + "\nWith file name: " + image_name)
		event.save()


	elif(event_type == "temp_trigger"):
		time_now=timezone.now()
		event=weather(weather_time=time_now, humidity=float(serialString[1]), temperature=float(serialString[2]))
		print("Temperature data generated for " + str(time_now.hour))
		event.save()

ser.close()
