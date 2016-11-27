from django import forms

class GitLink(forms.Form):
    link=forms.CharField(max_length = 100)
    pname= forms.CharField(max_length=80)

class IP(forms.Form):
    inp=forms.CharField(max_length=80)
    #out=forms.CharField(max_length=80)

class Saver(forms.Form):
    out=forms.CharField(max_length=200)
    nm=forms.CharField(max_length=200)