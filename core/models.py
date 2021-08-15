from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE, DO_NOTHING
from django.db.models.fields import BooleanField, DateTimeField, TimeField

class User(AbstractUser):
    display_name = models.CharField(max_length=200, default="preferred name", blank=True, null=True)
    legal_name = models.CharField(max_length=200, default="full legal name", blank=True, null=True)
    pronouns = models.CharField(max_length=200, default="pronouns", blank=True, null=True)
    availability = models.TextField(max_length=500, default='availability', blank=True, null=True)
    email = models.EmailField(max_length=200, null=True, blank=True, default="e-mail address")
    telephone = models.CharField(max_length=250, default="10-digit phone number", blank=True, null=True)
    address2 = models.CharField(max_length=50, default="Address 2", blank=True, null=True)
    city = models.CharField(max_length=50, default="City", blank=True, null=True)
    state = models.CharField(max_length=50, default="State", blank=True, null=True)
    zipcode = models.CharField(max_length=10, default="Zipcode", blank=True, null=True)
    user_status = models.CharField(max_length=50, default="permissions status", blank=True, null=True)
    intake_status = models.CharField(max_length=50, default="volunteer status", blank=True, null=True)
    preferred_event = models.TextField(max_length=500, default="preferred events", blank=True, null=True)

class Event(models.Model):
    id = models.CharField(max_length=250, primary_key=True, editable=False)
    event_header = models.CharField(max_length=250)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    type = models.CharField(max_length=250)
    description = models.TextField()

class Document(models.Model):
    id = models.CharField(max_length=250, primary_key=True)
    doc_header = models.CharField(max_length=250)
    summary = models.TextField(null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    url = models.URLField(max_length=200, null=True, blank=True)
    required = models.BooleanField(null=True, blank=True, default=None)

class Alert(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    alert_header = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

class Note(models.Model):
    id = models.CharField(max_length=200, null=False, blank=False, primary_key=True)
    text = models.TextField(null=True, blank=True)

class VolunteerSlot(models.Model):
    id = models.TextField(primary_key=True)
    vslot_text = models.CharField(max_length=250)
    event = models.ForeignKey(Event, on_delete=DO_NOTHING, related_name="event_slots")
    time = models.DateTimeField(null=True, blank=True)

class StatusBar(models.Model):
    id = BooleanField(default=False, primary_key=True)
    incomplete = BooleanField(default=False)
    pending = BooleanField(default=False)
    approved = BooleanField(default=False)
    complete = BooleanField(default=False)

class Tag(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    tag_text = models.CharField(max_length=250)
    event = models.ForeignKey(Event, on_delete=DO_NOTHING, related_name="event_tagged")  
