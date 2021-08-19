from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE, DO_NOTHING
from django.db.models.fields import AutoField, BooleanField, DateTimeField, TimeField
from django.db.models.fields.related import OneToOneField
from phone_field import PhoneField


class User(AbstractUser):
    display_name = models.CharField(max_length=200, default="preferred name", blank=True, null=True)
    legal_name = models.CharField(max_length=200, default="full legal name", blank=True, null=True)
    pronouns = models.CharField(max_length=200, default="pronouns", blank=True, null=True)
    availability = models.TextField(max_length=500, default='availability', blank=True, null=True)
    email = models.EmailField(max_length=200, null=True, blank=True, default="e-mail address")
    telephone = PhoneField(blank=True, help_text='Contact phone number')
    address2 = models.CharField(max_length=50, default="Address 2", blank=True, null=True)
    city = models.CharField(max_length=50, default="City", blank=True, null=True)
    state = models.CharField(max_length=50, default="State", blank=True, null=True)
    zipcode = models.CharField(max_length=10, default="Zipcode", blank=True, null=True)
    user_status = models.CharField(max_length=50, default="permissions status", blank=True, null=True)
    intake_status = models.CharField(max_length=50, default="volunteer status", blank=True, null=True)
    preferred_event = models.TextField(max_length=500, default="preferred events", blank=True, null=True)

class Event(models.Model):
    user = models.ManyToManyField(User, related_name="event_user")
    eventpk = models.AutoField(primary_key=True, default=None)
    event_header = models.CharField(max_length=250)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    type = models.CharField(max_length=250)
    description = models.TextField()

class Document(models.Model):
    user = models.ManyToManyField(User, related_name="document_user")
    docpk = models.AutoField(primary_key=True, default=None)
    doc_header = models.CharField(max_length=250)
    summary = models.TextField(null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    url = models.URLField(max_length=200, null=True, blank=True)
    required = models.BooleanField(null=True, blank=True, default=None)

class Alert(models.Model):
    user = models.ManyToManyField(User, related_name="alert_creator")
    alertpk = models.AutoField(primary_key=True, default=None)
    alert_header = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    event = models.ManyToManyField(Event, related_name="announcementevent", blank=True, default=None)

class Note(models.Model):
    user = models.ManyToManyField(User, related_name="note_creator")
    notepk = models.AutoField(primary_key=True, default=None)
    text = models.TextField(null=True, blank=True)

class VolunteerSlot(models.Model):
    user = models.ManyToManyField(User, related_name="event_volunteer", blank=True, default=None)
    slotpk = models.AutoField(primary_key=True, default=None)
    vslot_text = models.CharField(max_length=250)
    event = models.ForeignKey(Event, on_delete=DO_NOTHING, related_name="event_slots")
    starttime = models.TimeField(null=True, blank=True)
    endtime = models.TimeField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)

class StatusBar(models.Model):
    user = models.OneToOneField(User, on_delete=DO_NOTHING, related_name="volunteers_status")
    statuspk = models.AutoField(primary_key=True, default=None)
    incomplete = BooleanField(default=False)
    pending = BooleanField(default=False)
    approved = BooleanField(default=False)
    complete = BooleanField(default=False)

class Tag(models.Model):
    user = models.ManyToManyField(User, related_name="tag_user")
    tagpk = models.AutoField(primary_key=True, default=None)
    tag_text = models.CharField(max_length=250)
    event = models.ForeignKey(Event, on_delete=DO_NOTHING, related_name="event_tagged")