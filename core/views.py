from .models import Alert, Document, Event, Note, StatusBar, Tag, User, VolunteerSlot
from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import status,authentication, permissions, generics
from rest_framework import mixins
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from .serializers import AlertSerializer, DocumentSerializer, EventSerializer, NoteSerializer, StatusBarSerializer, TagSerializer, UserSerializer, VolunteerSlotSerializer
from core import serializers

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class NoteList(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class DocumentList(generics.ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class DocumentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class AlertList(generics.ListCreateAPIView):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer

class AlertDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer

class VolunteerSlotList(generics.ListCreateAPIView):
    queryset = VolunteerSlot.objects.all()
    serializer_class = VolunteerSlotSerializer

class VolunteerSlotDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = VolunteerSlot.objects.all()
    serializer_class = VolunteerSlotSerializer

class StatusList(generics.ListCreateAPIView):
    queryset = StatusBar.objects.all()
    serializer_class = StatusBarSerializer

class StatusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StatusBar.objects.all()
    serializer_class = StatusBarSerializer

class TagList(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
























