from django import forms

class GitLink(forms.Form):
    link=forms.CharField(max_length = 100)
    pname= forms.CharField(max_length=80)

class IP(forms.Forms):
    input=forms.CharField(max_length=200)
