from pyrogram import client, filters
from pyrogram.handlers import MessageHandler
from commands import *


if __name__ == '__main__':
    
    # WaterMark Command
    @app.on_message(filters.command("wm"))
    async def wm_command(client, message):
        await WaterMark(client=client, message=message)
        # print("wm")
    
    app.run()