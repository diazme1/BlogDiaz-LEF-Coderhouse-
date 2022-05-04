from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class UserRegister_form(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirme su contraseña", widget=forms.PasswordInput)

    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")

    class Meta:
        
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
        help_text = {k: "" for k in fields}

class UserEdit_form(UserCreationForm):

    email = forms.EmailField(label="Modificar E-mail")
    first_name = forms.CharField(label="Nombre", required=False)
    last_name = forms.CharField(label="Apellido", required=False)
    password1 = forms.CharField(label='Nueva contraseña', widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label='Confirme su contraseña', widget=forms.PasswordInput, required=False)

    class Meta:
        
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']
        help_text = {k: "" for k in fields}

class Avatar_form(forms.Form):

    img = forms.ImageField()

class AboutUser_form(forms.Form):

    bio = forms.CharField(widget=forms.Textarea, label='Biografía', required=False)
    instagram = forms.URLField(required=False, label='Instagram')
    facebook = forms.URLField(required=False, label='Facebook')
    twitter = forms.URLField(required=False, label='Twitter')

class Chat_form(forms.Form):
    
    body = forms.CharField(widget=forms.Textarea, label="")

class ChangePassword_form(forms.Form):

    password1 = forms.CharField(label="Nueva contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirme su contraseña", widget=forms.PasswordInput)

    class Meta:
        
        model = User
        fields = ['password1', 'password2']
        help_text = {k: "" for k in fields}