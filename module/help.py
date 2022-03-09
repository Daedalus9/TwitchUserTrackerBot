from var.text import HELP_MESSAGE

def help(update, context):
    chat_id=update.effective_chat.id
    context.bot.send_message(chat_id, HELP_MESSAGE)