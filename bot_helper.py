import telebot
from telebot import types


bot = telebot.TeleBot('BOT-TOKEN')


@bot.message_handler(commands = ['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text = 'Мой GitHub', url = 'https://github.com/KirillKrutski')
    markup.add(btn1)
    bot.send_message(message.from_user.id, "По кнопке ниже можно перейти на мой GitHub, для ознакомления с моими работами в сфере программирования", reply_markup=markup)
bot.polling(none_stop=True, interval=0)