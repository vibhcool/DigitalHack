from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import os
import subprocess
import json
from django.urls import reverse

from .api_do import my_server
from only_app.forms import GitLink,IP,Saver

serv=my_server()

def index(request):
    auth = request.body
    access_token = request.GET.get('code')
    
    if access_token == None:
        return HttpResponseRedirect(reverse('only_app:login'))
    else:
        serv.api_token=access_token
        request.session['access_token'] = access_token
    
    return render( request, 'Temp/main.html')

def control_panel( request):
    
    #power-on existing or new server    
    if request.GET.get( 'droplet')!=None:
        d_id = request.GET.get( 'code')
        serv.open_server( d_id)
    else:
        serv.new_server()
    serv.server_on()

    #authenticate
    link = serv.server_get_ip
    subprocess.call( ["ssh", "root@", link ])


def login(request):
    login_link=my_server.login_link

    return render(request, 'Temp/login.html', {'login_link': login_link })

def openTer(request):
    if request.method == 'POST':
        ip=IP(request.POST)
        if ip.is_valid():

            inp=ip.cleaned_data.get('inp')
            out=" "
            inp=inp.split()
            if inp[0]=="cd":
                os.chdir(inp[1])
            elif (inp[0]=="gedit")or(inp[0]=="vim")or(inp[0]=="nano"):
                #pop=subprocess.Popen("cat < "+inp[1])
                file=open(inp[1])
                pop=file.read()
                file.close()
                return render(request, 'Temp/editer.html',{"fnm":inp[1],"pop":pop})
            else:
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

"""
def editer(request):
    p = subprocess.Popen(, stdout=subprocess.PIPE)

    return render(request, 'Temp/editer.html')

def getTer(request):
    #server code
    serv=my_server()
    if(i==1):
        #new server         
        serv.server_create()
        did=serv.droplet.id #to save in database, this is droplet id
        serv.server_on()
        subprocess.call(["ssh","root@",link])
    elif(i==2):
        #restore server
    #to here
    if request.method == 'POST':
        if gitlink!=None            
            gitlink=GitLink(request.POST)
            if gitlink.is_valid():
                link = gitlink.cleaned_data.get('link')
                pname= gitlink.cleaned_data.get('pname')
            subprocess.call(["git","clone",link])
            os.chdir(pname)
            subprocess.call(["ls"])
    return render
"""


def editsave(request):
    if request.method == 'POST':
        s= Saver(request.POST)
        if s.is_valid():
            wrt=s.cleaned_data.get('out')
            fnm=s.cleaned_data.get('nm')
            file=open(fnm,'w')
            file.write(wrt)
            file.close()

    return render(request, 'Temp/term.html', {"out": " "})
