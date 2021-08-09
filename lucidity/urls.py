from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from django.views.generic import ListCreateAPIView
from django.contrib.auth.models import User
from core.serializers import UserSerializer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include ('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('users/', ListCreateAPIView.as_view(queryset=User.objects.all(), serializer_class=UserSerializer), name='volunteer-list'),

]
