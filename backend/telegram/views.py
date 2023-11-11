from django.http import JsonResponse
from django.shortcuts import render
from .tg import tg
from .validators import returnPosts

async def main(request):
    try:
        posts = await returnPosts(request)
        if type(posts) == list:
            return JsonResponse({"posts": posts})
        elif type(posts) == dict:
            return JsonResponse(posts)
        else:
            return JsonResponse({"err": "unknown error"})
    except:
        return JsonResponse({"err": "unknown error"})