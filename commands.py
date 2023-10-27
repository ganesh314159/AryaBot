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














