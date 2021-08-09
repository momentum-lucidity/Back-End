from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from django.views.generic import ListCreateAPIView
from django.contrib.auth.models import User
from core.serializers import UserSerializer
from core.views import user_profile, views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include ('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('volunteers/', views.user_list, name="volunteer_details"),
    path('volunteers/<int:pk>/', views.user_profile, name="volunteer_profile"),

]
