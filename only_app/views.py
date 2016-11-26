from django.shortcuts import render
from django.http import HttpResponse
import os
import subprocess

from .api_do import my_server
from only_app.forms import GitLink

def index(request):
    return render(request, 'Temp/main.html')

def ansible(request):
    #os.system("ls")
    return HttpResponse("running")

def getTer(request):
    if request.method == 'POST':
        gitlink=GitLink(request.POST)
        if gitlink.is_valid():
            link = gitlink.cleaned_data.get('link')
            pname= gitlink.cleaned_data.get('pname')
    subprocess.call(["git","clone",link])
    subprocess.call(["cd",pname])
    subprocess.call(["ls"])
    return HttpResponse("running")