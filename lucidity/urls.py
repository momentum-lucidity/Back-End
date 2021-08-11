from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from django.conf.urls import url
from django.contrib.auth.models import User
from core.serializers import UserSerializer
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include ('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('volunteers/', views.user_list),
    path('volunteers/<int:pk>/', views.user_profile),
    path('user/create/', views.registration),
    path('event/', views.event),
    path('event/<int:pk>/', views.event)
]
