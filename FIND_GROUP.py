import telebot

CHAVE_API = "6220194716:AAEARuQ9WIa9z37xIhYyVVjLR5U7UhYJ-Qw"

bot = telebot.TeleBot(CHAVE_API)

def verificar(mensagem):
    if mensagem.text == "AAAAA":
        return True
    else:
        return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    bot.reply_to(mensagem, "Oi TESTE2")


bot.polling()
