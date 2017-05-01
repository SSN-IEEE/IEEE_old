from django.conf.urls import url
from . import views

app_name='ieeestudent'

urlpatterns = [
    url(r'^home/$', views.index, name='index'),
    url(r'^home/events/2015/$', views.events_2015, name='events_2015'),
    url(r'^home/events/2016/$', views.events_2016, name='events_2016'),
    url(r'^home/events/2017/$', views.events_2017, name='events_2017'),
    url(r'^home/events/$', views.events, name='events'),
    url(r'^home/gallery/$', views.gallery, name='gallery'),
    url(r'^home/about/$', views.about, name='about')
]