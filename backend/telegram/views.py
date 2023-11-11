from django.http import JsonResponse
from django.shortcuts import render
from .tg import tg
from .validators import returnPosts

async def getPostsTG(request):
    try:
        posts = await returnPosts(request)
        if type(posts) == list:
            return JsonResponse({"posts": posts})
        elif type(posts) == dict:
            return JsonResponse(posts)
        else:
            print(posts)
            return JsonResponse({"err": "unknown error"})
    except Exception as e:
        print(e)
        return JsonResponse({"err": "unknown error"})