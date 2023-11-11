from django.urls import path
from geo.views import getGeoInfo

urlpatterns = [
    path("", getGeoInfo)
]
