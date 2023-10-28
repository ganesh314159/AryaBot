from pyrogram import Client
import os

async def progress(current, total, client, message):
    print(f"{current*100 / message.reply_to_message.document.file_size:.1f}%")

async def DownloadFile(client, message, app):
    # print('Downloading')
    fmid = message.reply_to_message_id
    cmid = message.id
    chat_id = message.chat.id
    # mess = await app.get_messages(chat_id, message_ids = fmid+1)
    # print(mess)
    # await app.send_message(chat_id=message.chat.id, text=f"R", reply_to_message_id=message.reply_to_message.id)
    while fmid < cmid:
        fmess = app.get_messages(chat_id = chat_id, message_ids = fmid)
        print(f'Downloading {fmess.document.file_name}')
        await app.download_media(message = fmess.document.file_id, file_name = fmess.document.file_name, progress=progress, progress_args=(client, message))
        fmid += 1
    print("Downloaded all files successfully!")
    
async def UploadFile(client, message, app):
    print('Uploading')
    path = "downloads/output"
    dir_list = os.listdir(path)
    for i in dir_list:
        print(f"Sending {i}")
        await app.send_document(chat_id=message.chat.id, document = f"downloads/output/{i}")
        