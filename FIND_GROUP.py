import os
from telegram.ext import Updater, CommandHandler

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Olá, eu sou um bot do Telegram!")

def main():
    TOKEN = os.environ.get('6248810171:AAHqayi78WsB0DJeo3PzzAXND5iWcsjDC68')
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
