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
    msg = bot.reply_to(message, """\
    Приветсвую в телеграм боте why_not. 
    Продолжая использовать данный бот,
    Вы подтверждаете тем сам мы что вам более 18 лет.
    """)
    bot.register_next_step_handler(msg, process_name_step, source_markup)


def process_name_step(message):
    try:
        chat_id = message.chat.id
        msg = bot.reply_to(chat_id, 'Выберите пункт')
        bot.register_next_step_handler(msg, process_age_step, chat_id)
    except Exception as e:
        bot.reply_to(message, 'oooops')


def process_age_step(message):
    try:
        chat_id = message.chat.id
        age = message.text
        if not age.isdigit():
            msg = bot.reply_to(message, 'Age should be a number. How old are you?')
            bot.register_next_step_handler(msg, process_age_step)
            return
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Male', 'Female')
        msg = bot.reply_to(message, 'What is your gender', reply_markup=markup)
        bot.register_next_step_handler(msg, process_sex_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')


def process_sex_step(message):
    try:
        chat_id = message.chat.id
        sex = message.text
        if (sex == u'Male') or (sex == u'Female'):
            user.sex = sex
        else:
            raise Exception()
        bot.send_message(chat_id, 'Nice to meet you ' + user.name + '\n Age:' + str(user.age) + '\n Sex:' + user.sex)
    except Exception as e:
        bot.reply_to(message, 'oooops')


bot.enable_save_next_step_handlers(delay=2)

bot.load_next_step_handlers()

bot.polling()
