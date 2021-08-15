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
        read_only_fields=['id']

class UrlSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Document
        fields = ['url']

class DocumentSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
    default=serializers.CurrentUserDefault()
)
    class Meta:
        model = Document
        fields = ['owner', 'doc_header', 'id', 'summary', 'body', 'url', 'required']
        read_only_fields=['owner', 'id']


class AlertSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
    default=serializers.CurrentUserDefault()
)
    class Meta:
        model = Alert
        fields = ['owner', 'id', 'alert_header', 'date','text']
        read_only_fields=['owner', 'id']


class NoteSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
    default=serializers.CurrentUserDefault()
)
    class Meta:
        model = Note
        fields = ['note_id', 'owner', 'text']
        read_only_fields=['note_id', 'owner']


class VolunteerSlotSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
    default=serializers.CurrentUserDefault()
)
    class Meta:
        model = VolunteerSlot
        fields = ['owner', 'vsslot_text', 'id', 'event', 'time']
        read_only_fields=['owner', 'id']


class StatusBarSerializer(serializers.ModelSerializer):
    required = serializers.ReadOnlyField(source='Document.required')
    owner = serializers.HiddenField(
    default=serializers.CurrentUserDefault()
)
    class Meta:
        model = StatusBar
        fields = ['owner', 'id', 'incomplete', 'pending', 'approved', 'complete', 'required']
        read_only_fields=['owner', 'id', 'required']


class TagSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
)
    class Meta:
        model = Tag
        fields = ['owner', 'id', 'tag_text']
        read_only_fields=['owner', 'id']