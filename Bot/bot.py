import telebot
from vars import bot_token, chat_id

bot = telebot.TeleBot(bot_token)

@bot.message_handler(content_types=['text'])
def start(message):
    bot.send_message(message.chat.id, message.chat.id)
    bot.register_next_step_handler(message, notify)

def notify(message):
    if message.chat.id in chat_id:
        bot.send_message(message.chat.id, "Теперь вам будут приходить уведомления.")
    else:
        bot.send_message(message.chat.id, "Ошибка")

bot.infinity_polling()
