from urllib import request
from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MakePost_form(forms.Form):

    owner = forms.CharField()
    autor = forms.CharField(max_length=40)
    email = forms.EmailField(max_length=40)
    titulo = forms.CharField(max_length=40)
    subtitulo = forms.CharField(max_length=100)
    cuerpo = forms.CharField(widget=forms.Textarea)
    imagen = forms.ImageField(required=False)

class LeaveComment_form(forms.Form):

    usuario = forms.CharField(max_length=50)
    body = forms.CharField(widget=forms.Textarea)
    post = forms.CharField(max_length=40, label='Post comentado')
    

    


