from rest_framework import serializers
from .models import User, Event, Document, Alert, Note, VolunteerSlot, StatusBar, Tag
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model

User = get_user_model()
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password', 'id', 'display_name','legal_name','pronouns', 'availability', 'email', 'telephone', 
        'address2', 'city','state','zipcode', 'user_status',
        'intake_status','preferred_event']
        read_only_field=['id']

class CreateUserSerializer(UserCreateSerializer):
        class Meta(UserCreateSerializer.Meta):
            model = User
            fields = ['username', 'password', 'id', 'display_name','legal_name','pronouns', 'availability', 'email', 'telephone', 
        'address2', 'city','state','zipcode', 'user_status',
        'intake_status','preferred_event']

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'event_header', 'date', 'start_time', 'end_time', 'type', 'description']

class UrlSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Document
        fields = ['url']

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['doc_header', 'id', 'summary', 'body', 'url', 'required']


class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = ['id', 'alert_header', 'date','text']


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['note_id', 'text']


class VolunteerSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = VolunteerSlot
        fields = ['vsslot_text', 'id', 'event', 'time']


class StatusBarSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusBar
        fields = ['id', 'incomplete', 'pending', 'approved', 'complete', 'required']
        read_only_fields=['required']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'tag_text']