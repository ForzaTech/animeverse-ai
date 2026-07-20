import asyncio
import json
import os
import re
import html

from news.anime import get_anime_news
from utils.telegram import send_message


SENT_FILE = "sent_news.json"


def clean_text(text):

    text = html.unescape(text)

    text = re.sub(
        r"<.*?>",
        "",
        text
    )

    text = text.lower()

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()



def load_sent_news():

    if not os.path.exists(SENT_FILE):
        return []

    try:
        with open(
            SENT_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

            if isinstance(data, list):
                return data

            return []

    except:

        return []



def save_sent_news(data):

    with open(
        SENT_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=4
        )



async def main():

    print("🌸 AnimeVerse Started")

    news_list = get_anime_news()


    if not news_list:

        print("❌ No news found")
        return



    sent_news = load_sent_news()


    print(
        "📦 Saved news:",
        len(sent_news)
    )


    new_count = 0



    for news in news_list:


        title = news["title"]

        news_id = clean_text(title)



        if news_id in sent_news:

            print(
                "⏩ Duplicate:",
                title
            )

            continue



        message = f"""
🌸 AnimeVerse

🔥 خبر جدید دنیای انیمه


🎬 عنوان:
{title}


📰 خلاصه:
{news['summary']}


🔗 منبع:
{news['link']}


━━━━━━━━━━━━━━
"""


        await send_message(message)



        sent_news.append(news_id)

        new_count += 1


        print(
            "✅ Sent:",
            title
        )



    save_sent_news(sent_news)



    print(
        f"🎉 Finished | New news: {new_count}"
    )



if __name__ == "__main__":

    asyncio.run(main())