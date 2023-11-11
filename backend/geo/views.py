from django.http import JsonResponse
from django.shortcuts import render

from .getGeoData import getData
def getGeoInfo(request):
    try:
        return JsonResponse({"adresses": getData(request)})
    except:
        return JsonResponse({"err":"unknown error"})
