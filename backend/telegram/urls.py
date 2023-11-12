from django.urls import path
from .views import getPostsTG, getOrSendCode

urlpatterns = [
    path('', getPostsTG), 
]
