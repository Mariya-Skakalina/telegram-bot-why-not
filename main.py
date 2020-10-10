import telebot
from telebot import types

API_TOKEN = '1286086072:AAGXY-EQBlQakoDjrYC97nUKteZosM91NHE'

bot = telebot.TeleBot(API_TOKEN)

source_markup = types.ReplyKeyboardMarkup()
source_markup_btn1 = types.KeyboardButton("Бронирование")
source_markup_btn2 = types.KeyboardButton("Цены")
source_markup_btn3 = types.KeyboardButton("Позвать кальянщика")
source_markup.row(source_markup_btn1, source_markup_btn2)
source_markup.row(source_markup_btn3)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    msg = bot.send_message(message.chat.id, """\
    Приветсвую в телеграм боте why_not. 
Продолжая использовать данный бот,
Вы подтверждаете тем сам мы что вам более 18 лет.
    """, reply_markup=source_markup)
    bot.register_next_step_handler(msg, name)


keyboards = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
keyboards_btn1 = types.KeyboardButton("16:00")
keyboards_btn2 = types.KeyboardButton("17:00")
keyboards_btn3 = types.KeyboardButton("18:00")
keyboards_btn4 = types.KeyboardButton("19:00")
keyboards_btn5 = types.KeyboardButton("20:00")
keyboards_btn6 = types.KeyboardButton("21:00")
keyboards_btn7 = types.KeyboardButton("22:00")
keyboards_btn8 = types.KeyboardButton("23:00")
keyboards_btn9 = types.KeyboardButton("Назад")
keyboards.row(keyboards_btn1, keyboards_btn2, keyboards_btn3, keyboards_btn4)
keyboards.row(keyboards_btn5, keyboards_btn6, keyboards_btn7, keyboards_btn8)
keyboards.row(keyboards_btn9)


def name(message):
    if message.text == 'Цены':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard_btn1 = types.KeyboardButton("Кальян")
        keyboard_btn2 = types.KeyboardButton("Пробка")
        keyboard_btn3 = types.KeyboardButton("Кальян с приставкой")
        keyboard_btn4 = types.KeyboardButton("Назад")
        keyboard.row(keyboard_btn1, keyboard_btn2)
        keyboard.row(keyboard_btn3)
        keyboard.row(keyboard_btn4)
        ngs = bot.send_message(message.chat.id, 'Цены на кальян', reply_markup=keyboard)
        bot.register_next_step_handler(ngs, price)
    elif message.text == "Бронирование":
        ngs = bot.send_message(message.chat.id, 'Выберите время:', reply_markup=keyboards)
        bot.register_next_step_handler(ngs, booking)
    elif message.text == "Позвать кальянщика":
        ngs = bot.send_message(message.chat.id, "Кальянщик придет к вам как только освободится")
        bot.register_next_step_handler(ngs, name)
    elif message.text == "Назад":
        msg = bot.send_message(message.chat.id, "Назад", reply_markup=source_markup)
        bot.register_next_step_handler(msg, send_welcome)


def price(mes):
    if mes.text == "Кальян":
        ngs = bot.send_message(mes.chat.id, "Цена кальяна 600 рублей")
        bot.register_next_step_handler(ngs, price)
    elif mes.text == "Пробка":
        ngs = bot.send_message(mes.chat.id, "Цена пробки 200 рублей")
        bot.register_next_step_handler(ngs, price)
    elif mes.text == "Кальян с приставкой":
        ngs = bot.send_message(mes.chat.id, "Цена кальяна с приставкой 700 рублей")
        bot.register_next_step_handler(ngs, price)
    elif mes.text == "Назад":
        ngs = bot.send_message(mes.chat.id, "Назад", reply_markup=source_markup)
        bot.register_next_step_handler(ngs, name)


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
        ngs = bot.send_message(mes.chat.id, 'Выберите стол:', reply_markup=keyboard)
        bot.register_next_step_handler(ngs, table)
    elif mes.text == "17:00":
        ngs = bot.send_message(mes.chat.id, 'Выберите стол:', reply_markup=keyboard)
        bot.register_next_step_handler(ngs, table)
    elif mes.text == "18:00":
        ngs = bot.send_message(mes.chat.id, 'Выберите стол:', reply_markup=keyboard)
        bot.register_next_step_handler(ngs, table)
    elif mes.text == "19:00":
        ngs = bot.send_message(mes.chat.id, 'Выберите стол:', reply_markup=keyboard)
        bot.register_next_step_handler(ngs, table)
    elif mes.text == "20:00":
        ngs = bot.send_message(mes.chat.id, 'Выберите стол:', reply_markup=keyboard)
        bot.register_next_step_handler(ngs, table)
    elif mes.text == "21:00":
        ngs = bot.send_message(mes.chat.id, 'Выберите стол:', reply_markup=keyboard)
        bot.register_next_step_handler(ngs, table)
    elif mes.text == "22:00":
        ngs = bot.send_message(mes.chat.id, 'Выберите стол:', reply_markup=keyboard)
        bot.register_next_step_handler(ngs, table)
    elif mes.text == "23:00":
        ngs = bot.send_message(mes.chat.id, 'Выберите стол:', reply_markup=keyboard)
        bot.register_next_step_handler(ngs, table)
    elif mes.text == "Назад":
        ngs = bot.send_message(mes.chat.id, "Назад", reply_markup=source_markup)
        bot.register_next_step_handler(ngs, name('Бронирование'))


def table(message):
    msg = bot.send_message(message.chat.id, "Стол заброанирован", reply_markup=source_markup)
    bot.register_next_step_handler(msg, name)


bot.polling()
