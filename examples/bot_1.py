from telegram.bot.bot import Bot


bot = Bot("token")

message = bot.get_last_message()


text, chat_id = message['message']['text'], message['message']['chat']['id']

bot.send_message(chat_id, text)
