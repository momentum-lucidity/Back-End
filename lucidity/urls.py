from django.contrib import admin
from django.urls import include, path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include ('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('volunteers/', views.user_list),
    path('volunteers/<int:id>/', views.user_profile),
    path('user/create/', views.registration),
    path('event/', views.event),
    path('event/<int:id>/', views.event),
    path('event/<int:id>/', views.eventDetail),
    path('event/<int:id>/edit/', views.eventEdit),
    path('event/<int:id>/delete/', views.eventDelete),
    path('notes/', views.noteList),
    path('notes/<int:id>/', views.noteDetail),
    path('notes/<int:id>/edit/', views.noteEdit),
    path('notes/<int:id>/delete/', views.noteDelete),
]
