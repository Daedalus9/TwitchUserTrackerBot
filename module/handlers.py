from telegram.ext import CommandHandler
from module.start import start
from module.track import track
from module.stop import stop

def cHandlers(updater):
    dispatcher=updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('track', track))
    dispatcher.add_handler(CommandHandler('stop', stop))