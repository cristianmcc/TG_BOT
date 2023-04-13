from telegram.ext import Updater

# Substitua a string "TOKEN" pelo seu token de acesso
updater = Updater("6248810171:AAHqayi78WsB0DJeo3PzzAXND5iWcsjDC68")

# Adicione mais código para definir os comandos do seu bot e outras funcionalidades
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Olá! Eu sou um bot CMC.")

# Criando o handler para o comando /start
start_handler = CommandHandler('start', start)

# Adicionando o handler ao bot
updater.dispatcher.add_handler(start_handler)

# Iniciando o bot
updater.start_polling()