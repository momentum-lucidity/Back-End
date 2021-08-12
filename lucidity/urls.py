from django.contrib import admin
from django.urls import include, path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include ('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('volunteers/', views.user_list),
    path('volunteers/<int:pk>/', views.user_profile),
    path('volunteers/<int:pk>/edit', views.profile_edit),
    path('volunteers/<int:pk>/delete', views.profile_delete),
    path('profile/create/', views.registration),
    path('profile/<int:pk>', views.registration),
    path('events/', views.event),
    path('events/<int:pk>/', views.eventDetail),
    path('events/<int:pk>/edit/', views.eventEdit),
    path('events/<int:pk>/delete/', views.eventDelete),
    path('notes/', views.noteList),
    path('notes/<int:pk>/', views.noteDetail),
    path('notes/<int:pk>/edit/', views.noteEdit),
    path('notes/<int:pk>/delete/', views.noteDelete),

]
