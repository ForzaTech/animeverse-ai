from telegram import Bot
from config import BOT_TOKEN, CHAT_ID


async def send_message(text):

    bot = Bot(token=BOT_TOKEN)

    await bot.send_message(
        chat_id=CHAT_ID,
        text=text
    )