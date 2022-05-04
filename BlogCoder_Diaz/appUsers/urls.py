from django.urls import path

from appUsers.views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path('accounts/login/', login_request, name='Login'),
    path('accounts/singup/', register_request, name='Register'),
    path('accounts/logout/', LogoutView.as_view(template_name='appUsers/logout.html'), name='Logout'),

    path('accounts/edituser/', edituser_request, name="EditarPerfil"),
    path('accounts/addavatar/', add_avatar, name='addAvatar'),

    path('accounts/profile/', open_profile, name='Profile'),
    path('accounts/userprofile/<usuario>', open_user_profile, name='OpenProfile'),

    path('chat/<usuario>', chatting, name='Chat'),
    path('inbox/', open_inbox, name='Inbox')

]