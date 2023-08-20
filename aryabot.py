import os
from telegram import Update
from telegram.ext import filters, ApplicationBuilder, CallbackContext, CommandHandler, MessageHandler
from commands import *

if __name__ == '__main__':
    application = ApplicationBuilder().token(token).build()
    # Start
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    # Chat id
    chatid_handler = CommandHandler('chatid', getChatID)
    application.add_handler(chatid_handler)
    
    
    
    application.run_polling()