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
        bot.register_next_step_handler(ngs, price)
    elif message.text == "Бронирование":
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        keyboard_btn1 = types.KeyboardButton("16:00")
        keyboard_btn2 = types.KeyboardButton("17:00")
        keyboard_btn3 = types.KeyboardButton("18:00")
        keyboard_btn4 = types.KeyboardButton("19:00")
        keyboard_btn5 = types.KeyboardButton("20:00")
        keyboard_btn6 = types.KeyboardButton("21:00")
        keyboard_btn7 = types.KeyboardButton("22:00")
        keyboard_btn8 = types.KeyboardButton("23:00")
        keyboard.row(keyboard_btn1, keyboard_btn2, keyboard_btn3, keyboard_btn4)
        keyboard.row(keyboard_btn5, keyboard_btn6, keyboard_btn7, keyboard_btn8)
        ngs = bot.send_message(message.chat.id, 'Цены на кальян', reply_markup=keyboard)
        bot.register_next_step_handler(ngs, booking)
    elif message.text == "Позвать кальянщика":
        bot.send_message(message.chat.id, "Кальянщик придет к вам как только освободится")


def price(mes):
    if mes.text == "Кальян":
        bot.send_message(mes.chat.id, "Цена кальяна 600 рублей")
    elif mes.text == "Пробка":
        bot.send_message(mes.chat.id, "Цена пробки 200 рублей")
    elif mes.text == "Кальян с приставкой":
        bot.send_message(mes.chat.id, "Цена кальяна с приставкой 700 рублей")


def booking(mes):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard_btn1 = types.KeyboardButton("1")
    keyboard_btn2 = types.KeyboardButton("2")
    keyboard_btn3 = types.KeyboardButton("3")
    keyboard_btn4 = types.KeyboardButton("4")
    keyboard_btn5 = types.KeyboardButton("5 cтол с приставкой")
    keyboard_btn6 = types.KeyboardButton("6")
    keyboard.row(keyboard_btn1, keyboard_btn2, keyboard_btn3)
    keyboard.row(keyboard_btn4, keyboard_btn5, keyboard_btn6)
    if mes.text == "16:00":
        ngs = bot.send_message(mes.chat.id, 'Выберите стол', reply_markup=keyboard)
        bot.register_next_step_handler(ngs, table)
    elif mes.text == "17:00":
        ngs = bot.send_message(mes.chat.id, 'Выберите стол', reply_markup=keyboard)
        bot.register_next_step_handler(ngs, table)
    elif mes.text == "18:00":
        ngs = bot.send_message(mes.chat.id, 'Выберите стол', reply_markup=keyboard)
        bot.register_next_step_handler(ngs, table)
    elif mes.text == "19:00":
        ngs = bot.send_message(mes.chat.id, 'Выберите стол', reply_markup=keyboard)
        bot.register_next_step_handler(ngs, table)
    elif mes.text == "20:00":
        ngs = bot.send_message(mes.chat.id, 'Выберите стол', reply_markup=keyboard)
        bot.register_next_step_handler(ngs, table)
    elif mes.text == "21:00":
        ngs = bot.send_message(mes.chat.id, 'Выберите стол', reply_markup=keyboard)
        bot.register_next_step_handler(ngs, table)
    elif mes.text == "22:00":
        ngs = bot.send_message(mes.chat.id, 'Выберите стол', reply_markup=keyboard)
        bot.register_next_step_handler(ngs, table)
    elif mes.text == "23:00":
        ngs = bot.send_message(mes.chat.id, 'Выберите стол', reply_markup=keyboard)
        bot.register_next_step_handler(ngs, table)


def table(message):
    bot.delete_message(message.chat.id, "Стол заброанирован")


bot.polling()
