from django.db import models
from datetime import date, datetime
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    autor = models.CharField(max_length=40)
    email = models.EmailField()
    fecha = models.DateField(auto_now_add=True)
    titulo = models.CharField(max_length=40, primary_key=True)
    subtitulo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='imagenesposts', null=True, blank=True)
    cuerpo = models.TextField("")

    def __str__(self) -> str:
        return f'{self.titulo} | {self.autor}'

class Comment(models.Model):

    usuario = models.CharField(max_length=50)
    body = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    post = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.usuario} | {self.post}'

    


