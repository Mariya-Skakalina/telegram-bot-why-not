import telebot
from telebot import types

API_TOKEN = '1286086072:AAGXY-EQBlQakoDjrYC97nUKteZosM91NHE'

bot = telebot.TeleBot(API_TOKEN)

source_markup = types.ReplyKeyboardMarkup()
source_markup_btn1 = types.KeyboardButton("Бронирование")
source_markup_btn2 = types.KeyboardButton("Цены")
source_markup_btn3 = types.KeyboardButton("Позвать кальянщика")
source_markup.row(source_markup_btn1,source_markup_btn2)
source_markup.row(source_markup_btn3)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message.chat.id, """\
    Приветсвую в телеграм боте why_not. 
Продолжая использовать данный бот,
Вы подтверждаете тем сам мы что вам более 18 лет.
    """, reply_markup=source_markup)
    # bot.register_next_step_handler(msg, source_markup)


bot.polling()
