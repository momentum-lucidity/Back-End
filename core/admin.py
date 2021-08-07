from django.contrib import admin
from .models import Document, Event, Note, User, Alert, VolunteerSlot
# Register your models here.
admin.site.register(User)
admin.site.register(Event)
admin.site.register(Document)
admin.site.register(Alert)
admin.site.register(Note)
admin.site.register(VolunteerSlot)
