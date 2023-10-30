from pyrogram import Client
from utils import *
import os


# Some Global Variables
HOME = os.path.expanduser("~")
with open(f'{HOME}/aryasecrets.txt', 'r') as file:
    content = file.read().replace('\n', ',')
    content = content.split(',')
    token = content[0]
    api_id = int(content[1])
    api_hash = str(content[2])
    
app = Client("Prajapatih", bot_token=token, api_id=api_id, api_hash=api_hash)

async def WaterMark(client, message):
    print("watermark")
    # print(message)
    # await app.send_message(chat_id=message.chat.id, text=f"{message}", reply_to_message_id=message.reply_to_message.id)
    await DownloadFile(client=client, message=message, app=app)

async def SendFile(client, message):
    print('Sending...')
    await UploadFile(client=client, message=message, app=app)

async def OCRPDF(client, message):
    chat_id = message.chat.id
    rmessid = message.reply_to_message.id
    try:
        file_name = message.reply_to_message.document.file_name
        file_id = message.reply_to_message.document.file_id
        size = message.reply_to_message.document.file_size
    except TypeError:
        pass
    dmess = f'''
File : 🗂️ {file_name} 🗂️
Status : Downloading...📤
Size : {(size/1048576)}MB
Progress : 0%
Source : 🌐 Telegram 🌐
'''
    await app.send_message(chat_id=chat_id, text=dmess, reply_to_message_id=rmessid)
    await app.download_media(message = file_id, file_name = file_name, progress=update_dmess, progress_args=(message, app))
    # Debug command
    await app.send_message(chat_id=chat_id, text="Passed test") 










