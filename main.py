import logging
from telegram.ext import Updater
from module.handlers import cHandlers

def main():
    TOKEN = 'TOKEN'
    updater= Updater(TOKEN, use_context=True)
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    cHandlers(updater)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()