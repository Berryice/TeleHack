from telegram.tg import tg
from django.utils.datastructures import MultiValueDictKeyError

async def returnPosts(request):
    try:
        posts = []
        if request.GET.get('search') and request.GET.get('username'):
            posts = await tg(request.GET['gname'], request.GET.get('search'), request.GET.get('username'))
        else:
            posts = await tg(request.GET['gname'], None, None)
        return posts
    except MultiValueDictKeyError:
        return {
            "err": "Not give param"
        }