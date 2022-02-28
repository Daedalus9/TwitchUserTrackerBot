import telegram
from telegram.ext import CommandHandler
from telegram.ext import Updater
import logging
import requests
import threading


ids=[]

TOKEN = 'TOKEN'
bot=telegram.Bot(TOKEN)
updater= Updater(TOKEN, use_context=True)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

dispatcher=updater.dispatcher

updater.start_polling()

def addId(update):
    chat_id=update.effective_chat.id
    ids.append(chat_id)

def deleteId(update):
    chat_id=update.effective_chat.id
    ids.remove(chat_id)

def search(update, context):
    chat_id=update.effective_chat.id
    us = open("list.txt", "r")
    if chat_id not in ids:
        context.bot.send_message(chat_id, "Attendi, potrebbero volerci fino a 5 minuti (per interrompere la ricerca corrente utilizza il comando /stop)")
        try:
            addId(update)
            user=update.message.text.split(" ",1)[1]
            print(user)
            counter=0
            for line in us:
                if chat_id in ids:
                    print("in corso...")
                    url = "https://tmi.twitch.tv/group/user/"+line.lower()[:-1]+"/chatters"
                    r=requests.get(url).json()
                    chat=r.get('chatters')['viewers']
                    if(user in chat):
                        context.bot.send_message(chat_id, user + " sta guardando " + line[:-1])
                        counter+=1
                        break
                else:
                    context.bot.send_message(chat_id, "Ricerca interrotta")
                    return
            if(counter<1):
                context.bot.send_message(chat_id, "L'utente " + user + " non sta guardando nessun canale Twitch, al momento")
            context.bot.send_message(chat_id, "Fine analisi")
            us.close()
            deleteId(update)
        except:
            context.bot.send_message(chat_id, "Nessun nickname specificato. Utilizza il comando come segue: /track nickname")
            deleteId(update)
    else:
        context.bot.send_message(chat_id, "Stai già facendo una ricerca. Attendi che finisca, prima di chiederne un'altra oppure utilizza il comando /stop per interrompere la ricerca corrente")
    
def start(update, context):
    chat_id=update.effective_chat.id
    context.bot.send_message(chat_id, "Benvenuto")

def stop(update, context):
    chat_id=update.effective_chat.id
    if chat_id in ids:
        deleteId(update)
    else:
        context.bot.send_message(chat_id, "Non stai facendo nessuna ricerca, al momento")
    
def track(update, context):
        chat_id=update.effective_chat.id
        thread = threading.Thread(target=search, args=(update, context))
        thread.start()

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('track', track))
dispatcher.add_handler(CommandHandler('stop', stop))

updater.idle()