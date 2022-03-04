from module.addDeleteId import deleteId, ids
from var.text import WARNING_NO_SEARCH_MESSAGE

def stop(update, context):
    chat_id=update.effective_chat.id
    if chat_id in ids:
        deleteId(update)
    else:
        context.bot.send_message(chat_id, WARNING_NO_SEARCH_MESSAGE)