from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.db.models.deletion import CASCADE
from django.db.models.fields import TimeField

class User(AbstractBaseUser):
    display_name: models.CharField(max_length=200)
    legal_name: models.CharField(max_length=200)
    pronouns: models.CharField(max_length=200)
    availability: models.TextField(max_length=500)
    email: models.EmailField(max_length=200)
    telephone: models.CharField()
    address1: models.CharField(max=50)
    address2: models.CharField(max=50)
    city: models.CharField(max=50)
    state: models.CharField(max=50)
    zipcode: models.CharField(max=10)
    user_status: models.CharField(max=50)
    intake_status: models.CharField(max=50)
    preferred_event: models.TextField(max_length=500)




    
