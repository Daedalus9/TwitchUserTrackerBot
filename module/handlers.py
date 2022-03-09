from telegram.ext import CommandHandler
from module.start import start
from module.track import track
from module.stop import stop
from module.help import help

def cHandlers(updater):
    dispatcher=updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('track', track))
    dispatcher.add_handler(CommandHandler('stop', stop))
    dispatcher.add_handler(CommandHandler('help', help))