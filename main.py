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
    msg = bot.send_message(message.chat.id, """\
    Приветсвую в телеграм боте why_not. 
Продолжая использовать данный бот,
Вы подтверждаете тем сам мы что вам более 18 лет.
    """, reply_markup=source_markup)
    bot.register_next_step_handler(msg, name)


def name(message):
    if message.text == 'Цены':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard_btn1 = types.KeyboardButton("Кальян")
        keyboard_btn2 = types.KeyboardButton("Пробка")
        keyboard_btn3 = types.KeyboardButton("Кальян с приставкой")
        keyboard.row(keyboard_btn1, keyboard_btn2)
        keyboard.row(keyboard_btn3)
        ngs = bot.send_message(message.chat.id, 'Цены на кальян', reply_markup=keyboard)
        bot.register_next_step_handler(ngs, prc)


def prc(mes):
    if mes.text == "Кальян":
        bot.send_message(mes.chat.id, "Цена кальяна 600 рублей")
    elif mes.text == "Пробка":
        bot.send_message(mes.chat.id, "Цена пробки 200 рублей")
    if mes.text == "Кальян с приставкой":
        bot.send_message(mes.chat.id, "Цена кальяна с приставкой 700 рублей")


bot.polling()
