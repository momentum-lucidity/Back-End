from django.contrib import admin
from .models import Event, User
# Register your models here.
admin.site.register(User)
admin.site.register(Event)