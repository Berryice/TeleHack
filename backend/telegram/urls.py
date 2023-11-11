from django.urls import path
from .views import getPostsTG

urlpatterns = [
    path('', getPostsTG)
]
