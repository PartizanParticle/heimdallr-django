from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /users/
    url(r'^$', views.index, name='index'),
]
