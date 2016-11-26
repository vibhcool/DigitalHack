from django import forms

class GitLink(forms.Form):
    link=forms.CharField(max_length = 100)
    pname= forms.CharField(max_length=80)
