from appBlog.views import *
from django.urls import path



urlpatterns = [
    
    path('', inicio, name='inicio'),
    path('pages/', pages, name='pages'),
    path('about/', aboutLEF, name="About"),

    path('pages/<titulo>', abrir_post, name='post'),

    path('search/', search_post, name='Buscar Post'),

    path('makepost/', makepost, name='New Post'),
    path('delete/<post_titulo>', deletepost, name='DeletePost'),
    path('post/update/<post_titulo>/', updatepost, name='UpdatePost'),

    path('commentform/<titulo>', leavecomment, name='New Comment'),

]


