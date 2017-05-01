from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View

def index(request):
    return render(request, 'ieeestudent/index.html')

def events_2015(request):
    return render(request, 'ieeestudent/events2015.html')

def events_2016(request):
    return render(request, 'ieeestudent/events2016.html')

def events_2017(request):
    return render(request, 'ieeestudent/events2017.html')

def events(request):
    return render(request, 'ieeestudent/events2017.html')

def gallery(request):
    return render(request, 'ieeestudent/gallery.html')

def about(request):
    return render(request, 'ieeestudent/about.html')