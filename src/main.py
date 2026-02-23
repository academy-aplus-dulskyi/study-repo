import telebot
import datetime
TOKEN = "token"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привіт! Я твій перший Telegram-бот 🤖")

@bot.message_handler(commands=['time'])
def time_message(message):
    bot.send_message(message.chat.id,datetime.datetime.now().strftime("%I:%M %p"))


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id," /start - hello message,"
                                     "/time - time message,")

bot.polling()
