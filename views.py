import os
from django.shortcuts import render
from datetime import datetime


def home_view(request):
    pages = [
        {'title': 'Home', 'url': 'home'},
        {'title': 'Current Time', 'url': 'current_time'},
        {'title': 'Workdir', 'url': 'workdir'},
    ]
    return render(request, 'app/home.html', {'pages': pages})


def current_time_view(request):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render(request, 'app/current_time.html', {'current_time': current_time})


def workdir_view(request):
    workdir = os.getcwd()
    files = os.listdir(workdir)
    return render(request, 'app/workdir.html', {'workdir': workdir, 'files': files})
