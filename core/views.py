from .models import Alert, Document, Event, Note, StatusBar, Tag, User, VolunteerSlot
from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import status,authentication, permissions, generics
from rest_framework import mixins
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import AlertSerializer, DocumentSerializer, EventSerializer, NoteSerializer, StatusBarSerializer, TagSerializer, UserSerializer, VolunteerSlotSerializer
from core import serializers
from core.permissions import CurrentUserOrAdmin, IsAdminOrReadOnly

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('display_name', 'email', 'availability')

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [CurrentUserOrAdmin]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class EventList(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrReadOnly, IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title', 'type', 'description')

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminOrReadOnly, IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class NoteList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class DocumentList(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrReadOnly, IsAuthenticated]
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class DocumentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminOrReadOnly, IsAuthenticated]
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class AlertList(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrReadOnly, IsAuthenticated]
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('date', 'event')

class AlertDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminOrReadOnly,IsAuthenticated]
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer

class VolunteerSlotList(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrReadOnly, IsAuthenticated]
    queryset = VolunteerSlot.objects.all()
    serializer_class = VolunteerSlotSerializer

class VolunteerSlotDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = VolunteerSlot.objects.all()
    serializer_class = VolunteerSlotSerializer

class StatusList(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrReadOnly, IsAuthenticated]
    queryset = StatusBar.objects.all()
    serializer_class = StatusBarSerializer

class StatusDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminOrReadOnly, IsAuthenticated]
    queryset = StatusBar.objects.all()
    serializer_class = StatusBarSerializer

class TagList(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrReadOnly, IsAuthenticated]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('text')

class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [CurrentUserOrAdmin, IsAuthenticated]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
























