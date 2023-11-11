from django.shortcuts import render
from django.http import JsonResponse
import vk_api
import json
import requests

access_token = 'vk1.a.v8xx1NAIwR6aPmWt-oXx5gq8l4VtpTdJFOR7hPGUvxtf9zQCGAhaOX_X7oTz45Kgyu_JTQHHWEeQmLs7AX5VDJEweHrwEg6YTvQ9PIOrAsapmjfbJYwyn__fdXO26ce3Vkb0QTebw5RGmX523gJZO_-sxSRdOaZ0kgdbO2xMUu0gdj8Jsk_8c5Kz7tDCrb30Mu10Jy8PEORm0ezPAqmg9w'
def user(request):
    print(2323232323)
    vk_session = vk_api.VkApi(login="79195876294", token=access_token)
    print(132422)
    vk = vk_session.get_api()
    '''request={
                "name":"Michman"
    }'''
    name = json.loads(request.body)["name"]
    print(name)
    try:
        usr = vk.users.get(user_id=name)[0]
    except Exception as e:
        print(name)
        print(e)
        return JsonResponse({"message": "ошибка в имени пользователя/id пользователя"})

    '''тут мы получаем айдишник '''
    response = requests.post(url=f"https://api.vk.com/method/execute",
                             data={
                                 "code": f"var id = API.utils.resolveScreenName({{'screen_name':'{name}'}});"
                                         "return id;",
                                 "access_token": access_token,
                                 "v": 5.126,
                             })
    try:
        '''приравниваем name к id
        если name и так равен id, то response.json()['response'] будет пустым'''
        name = response.json()['response']['object_id']

    except Exception:
        pass
    response = requests.post(url=f"https://api.vk.com/method/execute",
                                 data={
                                     "code": f"var usr = API.users.getFollowers({{'owner_id': '{name}'}});"
                                             "var b= usr.items;"
                                             "var followers = API.users.get({'user_ids':b});"
                                             "return followers;",
                                     "access_token": access_token,
                                     "v": 5.126,
                                 })
    # print(response.json())
    return JsonResponse({"user_info":usr,
                         'followers':response.json()['response']})



def group(request):
    '''request={
                "name":"meido4ka"
    }'''
    vk_session = vk_api.VkApi(login="79195876294", token=access_token)
    vk = vk_session.get_api()
    name = json.loads(request.body)["name"]
    try:
        group = vk.groups.getById(group_id=name)[0]
        return JsonResponse(group)
    except Exception:
        return JsonResponse({"message":"ошибка в имени/id сообщества"})
