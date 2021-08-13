from django.contrib import admin
from django.urls import include, path
from core import view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include ('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserList.as_view()),
    path('events/', views.EventList.as_view()),
    path('events/<int:pk>/', views.EventDetail.as_view()),
    path('notes/', views.NoteList.as_view()),
    path('notes/<int:pk>/', views.NoteDetail.as_view()),
    path('docs/', views.DocumentList.as_view()),
    path('docs/<int:pk>/', views.DocumentList.as_view()),
    path('announcements/', views.AlertList.as_view()),
    path('announcements/<int:pk>/', views.AlertDetail.as_view()),
    path('volunteerops/', views.VolunteerSlotList.as_view()),
    path('volunteerops/<int:pk>/', views.VolunteerSlotDetail.as_view()),
    path('status/', views.StatusList.as_view()),
    path('status/<int:pk>/', views.StatusDetail.as_view()),
    path('tags/', views.TagList.as_view()),
    path('tags/<int:pk>/', views.TagDetail.as_view()),
]

