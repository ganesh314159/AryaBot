import telegram
from telegram import Update
from telegram.ext import filters, ApplicationBuilder, CallbackContext, CommandHandler, MessageHandler, ContextTypes
import os

# Some Global Variables
HOME = os.path.expanduser("~")
with open(f'{HOME}/aryasecrets.txt', 'r') as file:
    content = file.read().replace('\n', ',')
    content = content.split(',')
    token = content[0]
    # openai_token = content[2]
    
CHAT_ID = ['-1001521285410']
TELEGRAM_BOT_USERNAME = 'prajapatih_bot'

# Start Command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if str(update.effective_chat.id) not in CHAT_ID :
        await context.bot.send_message(update.effective_chat.id, text="मन्त्राः अत्र न कार्यं कुर्वन्ति।")
        return
    mess_id = update.effective_message.message_id
    mess = '''
नमस्ते मम नाम प्रजापतिः।
अहं भवतः कथं साहाय्यं कर्तुं शक्नोमि?
'''

    await context.bot.send_message(update.effective_chat.id, reply_to_message_id=mess_id, text=mess)



async def getChatID(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = str(update.effective_chat.id)
    mess_id = update.effective_message.message_id
    user = update.effective_user.username
    await context.bot.send_message(chat_id, reply_to_message_id=mess_id, text=f"Chat id of this chat is '{chat_id}'.")