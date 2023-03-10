import telebot
from config import token

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	print(message.chat.id)
	bot.send_message(message.chat.id, message.text)

bot.infinity_polling()