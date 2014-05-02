from django.contrib import admin
from .models import SocialNetwork, Email, Phone

admin.site.register(SocialNetwork)
admin.site.register(Email)
admin.site.register(Phone)