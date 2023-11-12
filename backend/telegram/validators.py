from telegram.tg import tg
from django.utils.datastructures import MultiValueDictKeyError

async def returnPosts(request, api_id, api_hash):
    try:
        posts = []
        if request.GET.get('username'):
            posts = await tg(request.GET['gname'], request.GET.get('search'), request.GET.get('username'), api_id, api_hash)
        else:
            posts = await tg(request.GET['gname'], None, None, api_id, api_hash)
        return posts
    except MultiValueDictKeyError:
        return {
            "err": "Not give param"
        }