from django.shortcuts import render
from django.http import HttpResponse
import os

def index(request):
    return render(request, 'Temp/main.html')

def ansible(request):
    #os.system("ls")
    return HttpResponse("running")