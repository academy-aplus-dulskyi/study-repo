import telebot

TOKEN = "token"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    text = message.text.lower()

    if "привіт" in text:
        bot.send_message(message.chat.id, "Привіт! 😊")

    elif "як справи" in text:
        bot.send_message(message.chat.id, "У мене все добре! А у тебе?")

    else:
        bot.send_message(message.chat.id, "Я поки що не розумію цю фразу 🤔")


bot.polling()
