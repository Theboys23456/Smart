from pyrogram import Client, filters
from pyrogram.types import Message
import os
import random
from datetime import datetime

API_ID = int(os.environ.get("API_ID", 21567814))
API_HASH = os.environ.get("API_HASH", "cd7dc5431d449fd795683c550d7bfb7e")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7548746598:AAGbd7Vyxw_EODmQsH83tTxW4fVd-xxJEOY")

app = Client("livergram-bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

RESPONSES = [
    "👋 Hey {name}, how can I assist you today?",
    "✅ Got your message, {name}!",
    "🔥 Working on it, {name}!",
    "🧠 Smart move, {name}!",
    "🕒 You messaged at {time}, we'll respond soon."
]

@app.on_message(filters.private & filters.text)
async def advanced_reply(client: Client, message: Message):
    name = message.from_user.first_name
    now = {datetime.now().strftime('%H:%M:%S')}
    reply_text = random.choice(RESPONSES).format(name=name, time=now)
    await message.reply(reply_text)

app.run()
