from module.addDeleteId import deleteId, ids

def stop(update, context):
    chat_id=update.effective_chat.id
    if chat_id in ids:
        deleteId(update)
    else:
        context.bot.send_message(chat_id, "Non stai facendo nessuna ricerca, al momento")