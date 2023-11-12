from django.shortcuts import render
from django.http import JsonResponse
import vk_api
import json
import requests

access_token = 'vk1.a.9cJgAwKJrhyQ1cnWdQj6Gs5Cs1zd4kbbP6EmfxlODLzUxNhcEIyM20dbojmip9uE-7E4xcSIdAiAkL-nrI3-azO0eL28Rcd7X203xktTvYnRKlCGk6bGLgP6At1JjBFvI5gFnrskaYC6WAaCIeYfji0Ay2xYHutj5rkVM2djkG6UikVj6e6Wu_XPEIavOynoKpcoamq-NQloF6ArZSgqEQ'
phone = '79097000636'
def user(request):
    vk_session = vk_api.VkApi(login=phone, token=access_token)
    vk = vk_session.get_api()
    '''request={
                "name":"Michman"
    }'''
    name = json.loads(request.body)["name"]
    name = name.replace('id', '')
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
                                     "code": f"var usr = API.users.getFollowers({{'owner_id': '{name}', 'count': '10'}});"
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
    vk_session = vk_api.VkApi(login=phone, token=access_token)
    vk = vk_session.get_api()
    name = json.loads(request.body)["name"]
    name = name.replace('public', '')
    try:
        group = vk.groups.getById(group_id=name)[0]
        return JsonResponse(group)
    except Exception:
        return JsonResponse({"message":"ошибка в имени/id сообщества"})
