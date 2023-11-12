from django.http import JsonResponse
from django.shortcuts import render
from telethon import TelegramClient
from .tg import tg
from .validators import returnPosts
from django.contrib.auth.models import AnonymousUser
from .models import PhoneNumber
from asgiref.sync import sync_to_async
from backend import tokens

api_id = tokens.tg_api_id 
api_hash = tokens.tg_api_hash

async def getPostsTG(request):
    try:
        posts = await returnPosts(request, api_id=api_id, api_hash=api_hash)
        if type(posts) == list:
            return JsonResponse({"posts": posts})
        elif type(posts) == dict:
            return JsonResponse(posts)
        else:
            print(posts)
            JsonResponse({"err": "unknown error"})
    except Exception as e:
        print(e)
        return JsonResponse({"err": "unknown error"})




async def getOrSendCode(request):
    if request.method == 'GET':
        phNum = await sync_to_async(PhoneNumber.objects.get, thread_sensitive=True)(user=request.user)
        if request.user.is_authenticated and phNum:
            client = TelegramClient('anon', api_id=api_id, api_hash=api_hash)
            await client.connect()
            await client.send_code_request(phNum)
        else:
            return JsonResponse({"err":"You not signin on admin panel or not create object PhoneNumber in admin panel"})
    if request.method == 'POST':
        code_input = request.POST.get('code_input')
        phNum = await sync_to_async(PhoneNumber.objects.get, thread_sensitive=True)(user=request.user)
        client = TelegramClient('anon', api_id=api_id, api_hash=api_hash)
        client.start(phone=phNum, password=code_input)
        return render(request, 'cool.html')
    else:
        return render(request, 'code_request.html')