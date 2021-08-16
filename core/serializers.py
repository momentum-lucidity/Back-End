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
        fields = ['user', 'eventpk', 'event_header', 'date', 'start_time', 'end_time', 'type', 'description']
        read_only_field=['user', 'eventpk']
class UrlSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Document
        fields = ['url']

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['user', 'doc_header', 'docpk', 'summary', 'body', 'url', 'required']
        read_only_field=['user','docpk']

class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = ['user', 'alertpk', 'alert_header', 'date','text']
        read_only_field=['user', 'alertpk']

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['user', 'notepk', 'text']
        read_only_field=['user', 'notepk']

class VolunteerSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = VolunteerSlot
        fields = ['user', 'vsslot_text', 'slotpk', 'event', 'time']
        read_only_field=['user', 'slotpk']

class StatusBarSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusBar
        fields = ['user', 'statuspk', 'incomplete', 'pending', 'approved', 'complete', 'required']
        read_only_fields=['user', 'required', 'statuspk']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['user', 'tagpk', 'tag_text', 'event']
        read_only_field=['user', 'tagpk', 'event']