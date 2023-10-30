from pyrogram import Client
import subprocess
import os

async def progress(current, total, client, message):
    print(f"{current*100 / message.reply_to_message.document.file_size:.1f}%")

async def upload_to_gdrive(file_name):
    path = os.getcwd()+'/downloads/output/'+f"{file_name}"
    # print("Uploading ")
    subprocess.Popen([f"gdrive", "files", "upload", f"{path}"])

async def DownloadFile(client, message, app):
    # print('Downloading')
    fmid = message.reply_to_message_id
    cmid = message.id
    chat_id = message.chat.id
    # mess = await app.get_messages(chat_id, message_ids = fmid+1)
    # print(mess)
    # await app.send_message(chat_id=message.chat.id, text=f"R", reply_to_message_id=message.reply_to_message.id)
    while fmid < cmid:
        fmess = await app.get_messages(chat_id = chat_id, message_ids = fmid)
        print(f'Downloading {fmess.document.file_name}')
        await app.download_media(message = fmess.document.file_id, file_name = fmess.document.file_name, progress=progress, progress_args=(client, message))
        fmid += 1
    print("Downloaded all files successfully!")
    
async def UploadFile(client, message, app):
    print('Uploading')
    path = "downloads/output"
    dir_list = os.listdir(path)
    for i in dir_list:
        print(f"Sending {i} on telegram...")
        await app.send_document(chat_id=message.chat.id, document = f"downloads/output/{i}")
        print(f"Uploadind {i} to Google drive...")
        await upload_to_gdrive(i)
        print(f"Uploaded {i} Sucessfully!")
        
async def update_dmess(current, total, message, app):
    chat_id = message.chat.id
    message_id = message.id
    file_name = message.reply_to_message.document.file_name
    size = message.reply_to_message.document.file_size
    # progress = 
    dmess = f'''
File : 🗂️ {file_name} 🗂️
Status : Downloading...📤
Size : {(size/1048576)}MB
Progress : {current*100 / size:.2f}%
Source : 🌐 Telegram 🌐
'''
    app.edit_message_text(chat_id, message_id, text=dmess)