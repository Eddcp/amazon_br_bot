from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import os

#Constants
PORT = int(os.environ.get('PORT', 5000))
API_KEY = os.getenv("API_KEY", "optional-default")
COMMANDS = """
    /link - Link para página inicial da Amazon
    /link_livros - Link para página de livros da Amazon
    /link_eletronicos - Link para página de eletrônicos da Amazon
    /ofertas_dia - Link para as ofertas do dia
"""
  
def start(update: Update, context: CallbackContext):
    
    update.message.reply_text(
       """Olá, bem vindo! Gostaria de ver as novidades da Amazon? Lista de comandos disponíveis :-
       {}
    /help - Dicas de como utilizar""".format(COMMANDS))


def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Esse bot tem o objetivo de fornecer links para categorias de produtos da amazon, comandos disponíveis:
    {}
    """.format(COMMANDS))

def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Desculpe, eu não reconheci você, você disse '%s'" % update.message.text)
  
def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Desculpe '%s' nao é um comando válido" % update.message.text)

def link_url(update: Update, context: CallbackContext):
    update.message.reply_text("https://amzn.to/3BSHqBq")
  
def books_link_url(update: Update, context: CallbackContext):
    update.message.reply_text("https://amzn.to/3BQqeN3")
  
def eletronics_link_url(update: Update, context: CallbackContext):
    update.message.reply_text("https://amzn.to/3t8ras9")

def day_offers(update: Update, context: CallbackContext):
    update.message.reply_text("https://amzn.to/3phnPWI")

def initializeHandlers(updater: Updater):
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('link', link_url))
    updater.dispatcher.add_handler(CommandHandler('link_livros', books_link_url))
    updater.dispatcher.add_handler(CommandHandler('link_eletronicos', eletronics_link_url))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_handler(CommandHandler('ofertas_dia', day_offers))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
    updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

def initializeBot(updater: Updater):
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=API_KEY,
                          webhook_url='https://amazonbrbot.herokuapp.com/' + API_KEY)

def main():
    updater = Updater(API_KEY,
                  use_context=True)
    initializeHandlers(updater)
    initializeBot(updater)  

if __name__ == '__main__':
    main()