import telethon
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError

api_id = "22998293"
api_hash = "bce9f7a7a22733fd12ebef3840b60e48"



async def tg(gname, search, username):
    print(type(search))
    client = TelegramClient('anon', api_id=api_id, api_hash=api_hash)
    posts = []
    await client.start()
    try:
        if search and username:
            async for message in client.iter_messages(gname, search=search, from_user=username):
                if message.text:
                    posts.append(message.text)
        else:
            async for message in client.iter_messages(gname):
                if message.text:
                    posts.append(message.text)
            posts.reverse()
    except SessionPasswordNeededError:
        password = input('enter your password: ')
        await client.start(password=password)
    finally:
        await client.disconnect()
    return posts