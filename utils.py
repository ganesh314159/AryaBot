from pyrogram import Client

async def progress(current, total, client, message):
    print(f"{current*100 / message.reply_to_message.document.file_size:.1f}%")

async def DownloadFile(client, message, app):
    print('Downloading')
    await app.download_media(message.reply_to_message.document.file_id, progress=progress, progress_args=(client, message))
    
async def UploadFile(client, message, app):
    print('Uploading')
    await app.send_document(chat_id=message.chat.id, document = "downloads/output/*")