from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
from django.db.models.fields import TimeField

class User(AbstractUser):
    display_name: models.CharField(max_length=200)
    legal_name: models.CharField(max_length=200)
    pronouns: models.CharField(max_length=200)
    availability: models.TextField(max_length=500)
    email: models.EmailField(max_length=200)
    telephone: models.CharField()
    address1: models.CharField(max_length=50)
    address2: models.CharField(max_length=50)
    city: models.CharField(max_length=50)
    state: models.CharField(max_length=50)
    zipcode: models.CharField(max_length=10)
    user_status: models.CharField(max_length=50)
    intake_status: models.CharField(max_length=50)
    preferred_event: models.TextField(max_length=500)


class Event(models.Model):
    user = models.ManyToManyField(User, related_name="volunteer")
    title = models.CharField(max_length=250)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    type = models.CharField(max_length=250)
    description = models.TextField()



    
