import telebot
import cherrypy
from telebot import types


API_TOKEN = '1286086072:AAGXY-EQBlQakoDjrYC97nUKteZosM91NHE'

WEBHOOK_HOST = '178.154.250.224'
WEBHOOK_PORT = 8443
WEBHOOK_LISTEN = '0.0.0.0'

WEBHOOK_SSL_CERT = './webhook_cert.pem'  # Путь к сертификату
WEBHOOK_SSL_PRIV = './webhook_pkey.pem'  # Путь к приватному ключу

WEBHOOK_URL_BASE = "https://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/%s/" % (API_TOKEN)


bot = telebot.TeleBot(API_TOKEN)


class WebhookServer(object):
    @cherrypy.expose
    def index(self):
        if 'content-length' in cherrypy.request.headers and \
           'content-type' in cherrypy.request.headers and \
           cherrypy.request.headers['content-type'] == 'application/json':
            length = int(cherrypy.request.headers['content-length'])
            json_string = cherrypy.request.body.read(length).decode("utf-8")
            update = telebot.types.Update.de_json(json_string)
            bot.process_new_updates([update])
            return ''
        else:
            raise cherrypy.HTTPError(403)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row(*[types.KeyboardButton(name) for name in ['Бронирование', 'Цены']])
    keyboard.row(*[types.KeyboardButton(name) for name in ['Позвать кальянщика']])
    msg = bot.send_message(message.chat.id, """\
    Приветсвую в телеграм боте why_not. 
Продолжая использовать данный бот,
Вы подтверждаете тем сам мы что вам более 18 лет.
    """, reply_markup=keyboard)
    bot.register_next_step_handler(msg, menu)


def menu(message):
    if message.text == '/start':
        send_welcome(message)
    elif message.text == 'Цены':
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
        keyboards = types.ReplyKeyboardMarkup(resize_keyboard=True)
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
        ngs = bot.send_message(message.chat.id, 'Выберите время:', reply_markup=keyboards)
        bot.register_next_step_handler(ngs, booking)
    elif message.text == "Позвать кальянщика":
        ngs = bot.send_message(message.chat.id, "Кальянщик придет к вам как только освободится")
        bot.register_next_step_handler(ngs, menu)
    # elif message.text == "Назад":
    #     keyboard = types.ReplyKeyboardMarkup()
    #     keyboard.row(*[types.KeyboardButton(name) for name in ['Бронирование', 'Цены']])
    #     keyboard.row(*[types.KeyboardButton(name) for name in ['Позвать кальянщика']])
    #     msg = bot.send_message(message.chat.id, "Назад", reply_markup=keyboard)
    #     bot.register_next_step_handler(msg, send_welcome)


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
        source_markup = types.ReplyKeyboardMarkup()
        source_markup_btn1 = types.KeyboardButton("Бронирование")
        source_markup_btn2 = types.KeyboardButton("Цены")
        source_markup_btn3 = types.KeyboardButton("Позвать кальянщика")
        source_markup.row(source_markup_btn1, source_markup_btn2)
        source_markup.row(source_markup_btn3)
        ngs = bot.send_message(mes.chat.id, "Назад", reply_markup=source_markup)
        bot.register_next_step_handler(ngs, menu)


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
        source_markup = types.ReplyKeyboardMarkup()
        source_markup_btn1 = types.KeyboardButton("Бронирование")
        source_markup_btn2 = types.KeyboardButton("Цены")
        source_markup_btn3 = types.KeyboardButton("Позвать кальянщика")
        source_markup.row(source_markup_btn1, source_markup_btn2)
        source_markup.row(source_markup_btn3)
        ngs = bot.send_message(mes.chat.id, "Назад", reply_markup=source_markup)
        bot.register_next_step_handler(ngs, menu)


def table(message):
    source_markup = types.ReplyKeyboardMarkup()
    source_markup_btn1 = types.KeyboardButton("Бронирование")
    source_markup_btn2 = types.KeyboardButton("Цены")
    source_markup_btn3 = types.KeyboardButton("Позвать кальянщика")
    source_markup.row(source_markup_btn1, source_markup_btn2)
    source_markup.row(source_markup_btn3)
    msg = bot.send_message(message.chat.id, "Стол заброанирован", reply_markup=source_markup)
    bot.register_next_step_handler(msg, menu)


bot.remove_webhook()

bot.set_webhook(url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH, certificate=open(WEBHOOK_SSL_CERT, 'r'))

# Disable CherryPy requests log
access_log = cherrypy.log.access_log
for handler in tuple(access_log.handlers):
    access_log.removeHandler(handler)


cherrypy.config.update({
    'server.socket_host': WEBHOOK_LISTEN,
    'server.socket_port': WEBHOOK_PORT,
    'server.ssl_module': 'builtin',
    'server.ssl_certificate': WEBHOOK_SSL_CERT,
    'server.ssl_private_key': WEBHOOK_SSL_PRIV
})

cherrypy.quickstart(WebhookServer(), WEBHOOK_URL_PATH, {'/': {}})