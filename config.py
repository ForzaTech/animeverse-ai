from dotenv import load_dotenv
import os


load_dotenv()


BOT_TOKEN = os.getenv("BOT_TOKEN")

TOKEN = BOT_TOKEN


CHAT_ID = int(
    os.getenv("CHAT_ID")
)


GEMINI_API_KEY = os.getenv(
    "GEMINI_API_KEY"
)


print(
    "TOKEN:",
    TOKEN[:10] if TOKEN else None
)

print(
    "CHAT:",
    CHAT_ID
)