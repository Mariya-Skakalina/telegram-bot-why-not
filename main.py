from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters


updater = Updater(token='1286086072:AAGXY-EQBlQakoDjrYC97nUKteZosM91NHE', use_context=True)

dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)


updater.start_polling()
