from django.shortcuts import render

import requests

# Импортируем переменные телеграм бота
from Bot.vars import bot_token, chat_id

# Задаём переменную сообщения от бота
# message = ''
# Отправляем сообщение через Telegram API
# requests.get(f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}')
