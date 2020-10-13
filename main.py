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


def keyboards(*args):
    keyboard = types.ReplyKeyboardMarkup()
    for key in args:
        keyboard.row(*[types.KeyboardButton(name) for name in key])
    return keyboard


@bot.message_handler(commands=['start'])
def send_welcome(message):

    msg = bot.send_message(message.chat.id, """\
    Приветсвую в телеграм боте why_not. 
Продолжая использовать данный бот,
Вы подтверждаете тем сам мы что вам более 18 лет.
    """, reply_markup=keyboards(['Бронирование', 'Цены'], ['Позвать кальянщика']))
    bot.register_next_step_handler(msg, menu)


def menu(message):
    if message.text == '/start':
        send_welcome(message)
    elif message.text == 'Цены':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        ngs = bot.send_message(message.chat.id, 'Цены на кальян', reply_markup=keyboards(['Кальян', 'Пробка'],
                                                                                         ['Кальян с приставкой'],
                                                                                         ['Назад']))
        bot.register_next_step_handler(ngs, price)
    elif message.text == "Бронирование":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        ngs = bot.send_message(message.chat.id, 'Выберите время:', reply_markup=keyboards(['16:00', '17:00', '18:00', '19:00'],
                                                                                          ['20:00', '21:00', '22:00', '23:00'],
                                                                                          ['Назад']))
        bot.register_next_step_handler(ngs, booking)
    elif message.text == "Позвать кальянщика":
        ngs = bot.send_message(message.chat.id, "Кальянщик придет к вам как только освободится")
        bot.register_next_step_handler(ngs, menu)


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
        ngs = bot.send_message(mes.chat.id, "Назад", reply_markup=keyboards(['Бронирование', 'Цены'], ['Позвать кальянщика']))
        bot.register_next_step_handler(ngs, menu)


booking_seat = {}


def booking(mes):
    if (mes.text == "16:00" or mes.text == "17:00" or mes.text == "17:00" or mes.text == "18:00"
            or mes.text == "19:00" or mes.text == "20:00" or mes.text == "21:00" or mes.text == "22:00"
            or mes.text == "23:00"):
        booking_seat['time'] = mes.text
        print(booking_seat['time'])
        ngs = bot.send_message(mes.chat.id, 'Выберите стол:', reply_markup=keyboards(['1', '2', '3'],
                                                                                     ['4', '5 cтол с приставкой', '6']))
        bot.register_next_step_handler(ngs, table)
    elif mes.text == "Назад":
        ngs = bot.send_message(mes.chat.id, "Назад", reply_markup=keyboards(['Бронирование', 'Цены'],
                                                                            ['Позвать кальянщика']))
        bot.register_next_step_handler(ngs, menu)
print(booking_seat['time'])

def table(message):
    msg = bot.send_message(message.chat.id, "Стол заброанирован", reply_markup=keyboards(['Бронирование', 'Цены'],
                                                                                         ['Позвать кальянщика']))
    bot.register_next_step_handler(msg, menu)


bot.remove_webhook()

bot.set_webhook(url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH, certificate=open(WEBHOOK_SSL_CERT, 'r'))


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