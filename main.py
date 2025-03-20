import telebot

TOKEN = "7293498502:AAHTOU5qcWEheLuaHty0_rTUY38wNTq1hoM"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: message.text.lower() == "bonjour")
def greet_user(message):
   username = message.from_user.first_name  # Retrieve user's first name
   bot.reply_to(message, f"Salut {username} !")

bot.polling()

