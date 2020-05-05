import telebot
# from . import views
# from .models import SendCatandprice

user_dict = {}

bot = telebot.TeleBot('1168539036:AAFt31_hCwD7Vds8m-2Aivzhxq3U6hDRTCc')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет')
    user = (chat.id)
    bot.send_message('-439177655', (user, 'Заявка от бота', bot.get_me().username), parse_mode="Markdown")

#@bot.message_healder()

bot.polling()