from django.shortcuts import render
from users.models import press_event
from tempinfo.models import weather
from collections import OrderedDict
from .forms import heightForm
from django.http import HttpResponseRedirect
from static import save_data as save

# Create your views here.

def index(request):
	return render(request, 'index.html')

def about(request):
	return render(request, 'about.html')

def thanks(request):
	return render(request, 'thanks.html')

def get_info(request):
	if request.method == 'POST':
        # create a form instance and populate it with data from the request:
		form = heightForm(request.POST)

		if form.is_valid():
			save.save_data(str(form.cleaned_data["door_height"]))
			return HttpResponseRedirect('/thanks/')

	else:
		form = heightForm()

	return render(request, 'forms.html', {'form': form})

def graphs(request):
	time_list = press_event.objects.order_by('press_time')
	sorted_dict = OrderedDict([('Monday',0),
				   ('Tuesday',0),
				   ('Wednesday',0),
				   ('Thursday',0),
				   ('Friday',0),
				   ('Saturday',0),
				   ('Sunday',0)])

	for event in time_list:
		day = event.press_time.strftime('%A')
		if day is not None:
			sorted_dict[day]+=1

	temp_list = weather.objects.order_by('weather_time')

	temp_data = temp_list[0:24]
	temp_dict = OrderedDict([])
	hour_count=-1*len(temp_data)+1
	for data in temp_data:
		temp_dict.update({str(hour_count):data})
		hour_count+=1


	context = {'sorted_times': sorted_dict, 'temp_data': temp_dict}

	return render(request, 'graphs.html', context)
