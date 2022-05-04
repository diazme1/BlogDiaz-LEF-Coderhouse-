from django.contrib import admin

from appUsers.models import Avatar, UserAbout, Chat

# Models registration-->
admin.site.register(Avatar)
admin.site.register(UserAbout)
admin.site.register(Chat)