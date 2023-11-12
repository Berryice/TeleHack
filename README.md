# TeleHack
## Urls
#### frontend: http://localhost:8080 - Именно его вам нужно открыть
#### backend: http://localhost:8000
## Admin
#### path: http://localhost:8000/admin/
#### root:root
### все токены в ./backend/backend/tokens.py просьба установить их перед запуском
- dadata_token - token для dadata
- vk_access_token - access token для вк api  
- vk_phone - номер телефона для вк
- tg_api_id - api id для телеграм
- tg_api_hash - api hash для телеграм
#### получение vk_access_token :
- создайте standalone приложение вк
- перейдите по ссылке, подставив свой client id https://oauth.vk.com/authorize?client_id={CLIENT_ID}&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=1024&response_type=token&v=5.126&state=123456 (CLIENT_ID - id вашего standalone приложения вк)
- вас перенаправит на ссылку, которая будет в адрессе содержат ваш access token
## Запуск приложения
### Терминал 1
- cd backend
- python -m venv venv
- Активируйте окружение (
    venv\Scripts\activate.bat - для Windows
    source venv/bin/activate - для Linux
)
- pip install -r requirements.txt
- python manage.py runserver
### Терминал 2
- cd frontend
- npm install
- npm run serve
## Telegram требует доп настройки в рантайме:
#### Как только вы попытаетесь получить информацию о какой-нибудь группе в тг в Терминал 1 появится призыв к вводу номера телефона, вам нужн его ввести, затем в тг вам придет сообщение с кодом, вам нужно будет его ввесты в Терминал 1. Если все сделанно верно функциональность веб приложения будет доступна полноценно. При этом у вас откроется сессия тг, если вы ее закроете, вам придется выполнять все действия начиная с 32 строки снова.
## в приложении с вк указывайте не ссылку, а id пользователя или никнэйм!