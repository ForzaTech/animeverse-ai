import asyncio
import json
import os
import re
import html
from datetime import datetime

from news.anime import get_anime_news
from news.manga import get_manga_news
from utils.telegram import send_message


SENT_FILE = "sent_news.json"



def clean_text(text):

    text = html.unescape(text)

    text = re.sub(
        r"<.*?>",
        "",
        text
    )

    return re.sub(
        r"\s+",
        " ",
        text.lower()
    ).strip()



def load_sent_news():

    if not os.path.exists(SENT_FILE):
        return []

    try:

        with open(
            SENT_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

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



def get_source(link):

    if "myanimelist" in link:
        return "MyAnimeList"

    if "animenewsnetwork" in link:
        return "Anime News Network"

    return "Unknown"



def create_message(news):

    category = news.get(
        "type",
        "news"
    )


    if category == "manga":
        category = "📚 Manga News"

    else:
        category = "🎬 Anime News"



    return f"""
🌸 AnimeVerse

{category}


🎬 عنوان:
{news['title']}


📝 خلاصه:
{news['summary']}


🌐 منبع:
{get_source(news['link'])}


🕒 زمان دریافت:
{datetime.now().strftime("%Y-%m-%d %H:%M")}


🔗 لینک:
{news['link']}


━━━━━━━━━━━━━━
"""



async def main():

    print("🌸 AnimeVerse Started")


    news_list = (
        get_anime_news()
        +
        get_manga_news()
    )


    sent_news = load_sent_news()


    print(
        "📦 Saved news:",
        len(sent_news)
    )


    new_count = 0



    for news in news_list:


        news_id = clean_text(
            news["title"]
        )


        if news_id in sent_news:

            print(
                "⏩ Duplicate:",
                news["title"]
            )

            continue



        await send_message(
            create_message(news)
        )


        sent_news.append(
            news_id
        )


        new_count += 1


        print(
            "✅ Sent:",
            news["title"]
        )



    save_sent_news(sent_news)


    print(
        f"🎉 Finished | New news: {new_count}"
    )



if __name__ == "__main__":

    asyncio.run(main())