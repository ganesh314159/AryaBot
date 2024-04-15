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
    
    # Download
    download_handler = CommandHandler('download', downloadFile)
    application.add_handler(download_handler)
    
    # OCR
    ocr_handler = CommandHandler('ocr', OCR)
    application.add_handler(ocr_handler)    
    
    application.run_polling()