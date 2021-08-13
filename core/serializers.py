
from rest_framework import serializers
from .models import User, Event, Document, Alert, Note, VolunteerSlot, StatusBar, Tag


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password', 'id', 'display_name','legal_name','pronouns', 'availability', 'email', 'telephone', 
        'address2', 'city','state','zipcode', 'user_status',
        'intake_status','preferred_event']
        read_only_field=['id']

class EventSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
    default=serializers.CurrentUserDefault()
)
    class Meta:
        model = Event
        fields = ['owner', 'title', 'date', 'start_time', 'end_time', 'type', 'description']
        read_only_fields=['owner']

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
        fields = ['owner', 'title', 'summary', 'body', 'url', 'required']
        read_only_fields=['owner']


class AlertSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
    default=serializers.CurrentUserDefault()
)
    class Meta:
        model = Alert
        fields = ['owner', 'title', 'date','text']
        read_only_fields=['owner']


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
        fields = ['owner', 'text_slot', 'event', 'time']
        read_only_fields=['owner']


class StatusBarSerializer(serializers.ModelSerializer):
    required = serializers.ReadOnlyField(source='Document.required')
    owner = serializers.HiddenField(
    default=serializers.CurrentUserDefault()
)
    class Meta:
        model = StatusBar
        fields = ['owner', 'unfinished', 'pending', 'approved', 'complete', 'required']
        read_only_fields=['owner', 'required']


class TagSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
)
    class Meta:
        model = Tag
        fields = ['owner', 'text']
        read_only_fields=['owner']