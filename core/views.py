from .models import Alert, Document, Event, Note, Tag, User
from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import status,authentication, permissions, generics
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from .serializers import AlertSerializer, DocumentSerializer, EventSerializer, NoteSerializer, TagSerializer, UserSerializer
from core import serializers


@api_view(['GET', 'POST'])
def user_list(request):

    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        serializer.is_valid()
        serializer.save(user=request.user)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def user_profile(request, pk):

    if request.method == 'GET':
        user = User.objects.get(id=pk)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)

        serializer.is_valid()
        serializer.save(user=request.user)
        return Response(serializer.data)

@api_view(['PUT'])
def profile_edit(request, pk):

    if request.method == 'PUT':
        edit = User.object.get(id=pk)
        serializer = UserSerializer(edit, data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)

@api_view(['DELETE'])
def profile_delete(request, pk):

    if request.method == 'DELETE':
        delete = User.objects.get(id=pk)
        delete.delete()
        return Response('This profile has been deleted')


@api_view(['GET', 'POST'])
def registration(request, *args, **kwargs):
    if request.method == 'GET':
        user = User.objects.get(pk=id)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def event(request):
    if request.method == 'GET':
        event = Event.objects.all()
        serializer = EventSerializer(event, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EventSerializer(data=request.data)
        serializer.is_valid()
        serializer.save(user=request.user)
        return Response(serializer.data)

@api_view(['GET'])
def eventDetail(request, pk):
    if request.method == 'GET':
        event = Event.objects.get(id=pk)
        serializer = EventSerializer(event, many=False)
        return Response(serializer.data)

@api_view(['PUT'])
def eventEdit(request, pk):
    if request.method == 'PUT':
        event = Event.objects.get(id=pk)
        serializer = EventSerializer(instance=event, data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)

@api_view(['DELETE'])
def eventDelete(request, pk):
    if request.method == 'DELETE':
        event = Event.objects.get(id=pk)
        event.delete()
        return Response('Event has been deleted')


@api_view(['GET', 'POST'])
def noteList(request):
    if request.method == 'GET':
        note = Note.objects.all()
        serializers = NoteSerializer(note, many=True)
        return Response (serializers.data)

    elif request.method == 'POST':
        serializer = NoteSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)

@api_view(['GET'])
def noteDetail(request, pk):
    if request.method == 'GET':
        note = Note.objects.get(id=pk)
        serializer = NoteSerializer(note, many=False)
        return Response(serializer.data)

@api_view(['PUT'])
def noteEdit(request, pk):
    if request.method == 'PUT':
        note = Note.objects.get(id=pk)
        serializer = NoteSerializer(note, data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)

@api_view(['DELETE'])
def noteDelete(request, pk):
    if request.method == 'DELETE':
        note = Note.objects.get(id=pk)
        note.delete()
        return Response('This note has been deleted')

@api_view(['GET', 'POST'])
def docList(request):
    if request.method == 'GET':
        documents = Document.objects.all()
        serializers = DocumentSerializer(documents, many=True)
        return Response(serializers.data)
    
    elif request.method == 'POST':
        serializer = DocumentSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)

@api_view(['GET'])
def docDetail(request, pk):
    if request.method == 'GET':
        document = Document.object.get(id=pk)
        serializer = DocumentSerializer(document, many=False)
        return Response(serializer.data)

@api_view(['PUT'])
def docEdit(request, pk):
    if request.method == 'PUT':
        document = Document.objects.get(id=pk)
        serializer = DocumentSerializer(document, data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)

@api_view(['DELETE'])
def docDelete(request, pk):
    if request.method == 'DELETE':
        document = Document.objects.get(id=pk)
        document.delete()
        return Response('Document has been deleted')

@api_view(['GET', 'POST'])
def alertList(request):
    if request.method == 'GET':
        alert = Alert.objects.all()
        serializers = AlertSerializer(alert, many=True)
        return Response(serializers.data)

    elif request.method == 'POST':
        serializer = AlertSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)

@api_view(['GET'])
def alertDetail(request, pk):
    if request == 'GET':
        alert = Alert.objects.get(id=pk)
        serializer = AlertSerializer(alert, many=False)
        return Response(serializer.data)

@api_view(['PUT'])
def alertEdit(request, pk):
    if request.method == 'PUT':
        alert = Alert.objects.get()
        serializer = AlertSerializer(alert, data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)

@api_view(['DELETE'])
def alertDelete(request, pk):
    if request.method == 'DELETE':
        alert = Alert.objects.get(id=pk)
        alert.delete()
        return Response('Alert has been deleted')

@api_view(['GET', 'POST'])
def tagList(request):
    if request.method == 'GET':
        tags = Tag.objects.all()
        serializers = TagSerializer(tags, many=True)
        return Response(serializers.data)

    elif request.method == 'POST':
        serializers = TagSerializer(data=request.data)
        serializers.is_valid()
        serializers.save()
        return Response(serializers.data)

@api_view(['GET'])
def tagDetail(request, pk):
    if request.method == 'GET':
        tag = Tag.objects.get(id=pk)
        serializer = TagSerializer(tag, many=False)
        return Response(serializer.data)

@api_view(['PUT'])
def tagEdit(request, pk):
    if request.method == 'PUT':
        tag = Tag.objects.get(id=pk)
        serializer = TagSerializer(tag, data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)

@api_view(['DELETE'])
def tagDelete(request, pk):
    if request.method == 'DELETE':
        tag = Tag.objects.get(id=pk)
        tag.delete()
        return Response('Tag deleted')














    








































