import requests
from module.addDeleteId import ids, addId, deleteId
from var.text import ERROR_NICKNAME, NOT_FIND_MESSAGE, SEARCH_MESSAGE, STOP_ANALYSIS_MESSAGE, STOP_SEARCH_MESSAGE, USER_TEXT, WARNING_MESSAGE, WATCH_TEXT

def search(update, context):
    chat_id=update.effective_chat.id
    message=update.message.text
    us = open("list.txt", "r")
    if chat_id not in ids:
        if(message!="/track"):
            context.bot.send_message(chat_id, SEARCH_MESSAGE)
            addId(update)
            user=update.message.text.split(" ",1)[1]
            counter=0
            for line in us:
                try:
                    if chat_id in ids:
                        url = "https://tmi.twitch.tv/group/user/"+line.lower()[:-1]+"/chatters"
                        r=requests.get(url).json()
                        chat=r.get('chatters')['viewers']
                        if(user in chat):
                            context.bot.send_message(chat_id, user + WATCH_TEXT + line[:-1])
                            counter+=1
                            break
                    else:
                        context.bot.send_message(chat_id, STOP_SEARCH_MESSAGE)
                        return
                except:
                    continue
            if(counter<1):
                context.bot.send_message(chat_id, USER_TEXT + user + NOT_FIND_MESSAGE)
            context.bot.send_message(chat_id, STOP_ANALYSIS_MESSAGE)
            us.close()
            deleteId(update)
        else:
            context.bot.send_message(chat_id, ERROR_NICKNAME)
    else:
        context.bot.send_message(chat_id, WARNING_MESSAGE)
    