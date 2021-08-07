from django.contrib import admin
from .models import Document, Event, Note, User, Alert
# Register your models here.
admin.site.register(User)
admin.site.register(Event)
admin.site.register(Document)
admin.site.register(Alert)
admin.site.register(Note)
