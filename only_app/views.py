from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'Temp/main.html')

def ansible(request):
    return HttpResponse("running")