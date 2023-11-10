from django.urls import path

from . import views

urlpatterns = [
    path('user/', views.user, name='user'),
    path('group/', views.group, name='group'),
]