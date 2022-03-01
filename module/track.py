from module.search import search
import threading

def track(update, context):
        thread = threading.Thread(target=search, args=(update, context))
        thread.start()