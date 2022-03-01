ids=[]
def addId(update):
    chat_id=update.effective_chat.id
    ids.append(chat_id)

def deleteId(update):
    chat_id=update.effective_chat.id
    ids.remove(chat_id)
