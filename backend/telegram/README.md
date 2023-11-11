# Telegram api module
### url localhost:8000/telegram/
### params: 
- gname* - identifier of channel
- search - keywords for search on channel
- username - identifier of user, which posts I will search by keyword
### Examples:
1) http://localhost:8000/telegram/?gname=gforrealmans&username=immicmen&search=квас
2) http://localhost:8000/telegram/?gname=gforrealmans
### If not search or username, then app use 2 option
### But u can leave search empty and u recive all posts of this user