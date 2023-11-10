from django.shortcuts import render
from django.http import JsonResponse
import vk_api
import json
access_token = 'vk1.a.v8xx1NAIwR6aPmWt-oXx5gq8l4VtpTdJFOR7hPGUvxtf9zQCGAhaOX_X7oTz45Kgyu_JTQHHWEeQmLs7AX5VDJEweHrwEg6YTvQ9PIOrAsapmjfbJYwyn__fdXO26ce3Vkb0QTebw5RGmX523gJZO_-sxSRdOaZ0kgdbO2xMUu0gdj8Jsk_8c5Kz7tDCrb30Mu10Jy8PEORm0ezPAqmg9w'
vk_session = vk_api.VkApi(login="79195876294", token=access_token)
vk = vk_session.get_api()

def user(request):
    '''request={
                "name":"Michman"
    }'''
    name = json.loads(request.body)["name"]
    try:
        usr = vk.users.get(user_id=name)[0]
        return JsonResponse(usr)
    except Exception:
        return JsonResponse({"message":"something went wrong"})

def group(request):
    '''request={
                "name":"meido4ka"
    }'''
    name = json.loads(request.body)["name"]
    try:
        group = vk.groups.getById(group_id=name)[0]
        return JsonResponse(group)
    except Exception:
        return JsonResponse({"message":"something went wrong"})
