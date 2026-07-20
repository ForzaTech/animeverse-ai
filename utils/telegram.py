import requests

from config import TOKEN, CHAT_ID


TELEGRAM_API = (
    f"https://api.telegram.org/bot{TOKEN}"
)



async def send_message(text):

    url = f"{TELEGRAM_API}/sendMessage"


    data = {

        "chat_id": CHAT_ID,

        "text": text,

        "parse_mode": "HTML"

    }


    response = requests.post(
        url,
        data=data
    )


    return response.json()



async def send_photo(photo, caption):

    url = f"{TELEGRAM_API}/sendPhoto"


    data = {

        "chat_id": CHAT_ID,

        "photo": photo,

        "caption": caption,

        "parse_mode": "HTML"

    }


    response = requests.post(
        url,
        data=data
    )


    return response.json()