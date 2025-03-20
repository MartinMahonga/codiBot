import os
from dotenv import load_dotenv
import telebot

load_dotenv()

token = os.getenv('TOKEN')
bot = telebot.TeleBot(token)

@bot.message_handler(func=lambda message: message.text.lower() == "bonjour")
def greet_user(message):
   username = message.from_user.first_name  # Retrieve user's first name
   bot.reply_to(message, f"Salut {username} !")

bot.polling()

