from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = int(os.getenv("CHAT_ID"))

print("TOKEN:", BOT_TOKEN[:10] if BOT_TOKEN else None)
print("CHAT:", CHAT_ID)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")