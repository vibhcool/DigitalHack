from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import os
import subprocess

from django.urls import reverse

from .api_do import my_server
from only_app.forms import GitLink,IP

def index(request):
    return render(request, 'Temp/main.html')

def openTer(request):
    if request.method == 'POST':
        ip=IP(request.POST)
        if ip.is_valid():

            inp=ip.cleaned_data.get('inp')

            inp=inp.split()
            p=subprocess.Popen(inp, stdout=subprocess.PIPE)
            out, err = p.communicate()
            return render(request, 'Temp/term.html', {"out":out})
        else:
            return HttpResponse("Form not valid")
    else:
        return render(request, 'Temp/term.html', {"out": " "})



def ansible(request):
    #os.system("ls")
    return HttpResponse("running")

def getTer(request):
    if request.method == 'POST':
        gitlink=GitLink(request.POST)
        if gitlink.is_valid():
            link = gitlink.cleaned_data.get('link')
            pname= gitlink.cleaned_data.get('pname')
        else:
            return HttpResponse("Form not valid")
    subprocess.call(["git","clone",link])
    os.chdir(pname)
    subprocess.call(["ls"])
    return HttpResponseRedirect(reverse('only_app:openTer'))