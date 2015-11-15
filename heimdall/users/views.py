
from django.shortcuts import render
from .models import press_event

# Create your views here.

def index(request):
	user_list=press_event.objects.order_by('-press_time')
	context={'user_list': user_list}
	return render(request, 'users/index.html', context)

