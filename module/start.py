def start(update, context):
    chat_id=update.effective_chat.id
    context.bot.send_message(chat_id, "Benvenuto! Utilizza il comando /track <nickname> per iniziare la ricerca")
