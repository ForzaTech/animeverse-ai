import asyncio
import json
import os
import re
import html
from datetime import datetime

from news.anime import get_anime_news
from news.manga import get_manga_news
from utils.telegram import send_message, send_photo
from utils.anilist import search_anime


SENT_FILE = "sent_news.json"



def clean_text(text):

    text = html.unescape(text)

    text = re.sub(
        r"<.*?>",
        "",
        text
    )

    text = re.sub(
        r"\s+",
        " ",
        text.lower()
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


    except Exception:

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



def create_message(news, anime_info=None):

    category = (
        "📚 Manga News"
        if news.get("type") == "manga"
        else
        "🎬 Anime News"
    )


    message = f"""
🌸 AnimeVerse

{category}


🎬 عنوان:
{news['title']}


📝 خلاصه:
{news['summary']}
"""


    if anime_info:

        message += f"""

━━━━━━━━━━━━

⭐ امتیاز:
{anime_info.get('score', 'N/A')}/100


🎭 ژانر:
{anime_info.get('genres', 'N/A')}


📺 قسمت‌ها:
{anime_info.get('episodes', 'N/A')}


📌 وضعیت:
{anime_info.get('status', 'N/A')}
"""


    message += f"""

━━━━━━━━━━━━

🌐 لینک:
{news['link']}


🕒 زمان:
{datetime.now().strftime("%Y-%m-%d %H:%M")}

━━━━━━━━━━━━
"""


    return message



async def main():

    print("🌸 AnimeVerse Started")


    news_list = (
        get_anime_news()
        +
        get_manga_news()
    )


    if not news_list:

        print("❌ No news found")

        await send_message(
            """
🌸 AnimeVerse

❌ دریافت خبرها با مشکل مواجه شد.
"""
        )

        return



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



        anime_info = None



        if news.get("type") == "anime":

            try:

                anime_info = search_anime(
                    news["title"]
                )


            except Exception as e:

                print(
                    "⚠️ AniList Error:",
                    e
                )



        message = create_message(
            news,
            anime_info
        )



        if (
            anime_info
            and anime_info.get("image")
        ):

            await send_photo(
                anime_info["image"],
                message
            )


            print(
                "🖼 Photo Sent:",
                news["title"]
            )


        else:

            await send_message(
                message
            )


            print(
                "📝 Text Sent:",
                news["title"]
            )



        sent_news.append(
            news_id
        )


        new_count += 1



    save_sent_news(
        sent_news
    )



    if new_count == 0:

        await send_message(
            """
🌸 AnimeVerse

⏳ بررسی جدیدترین اخبار انجام شد.

❌ خبر جدیدی پیدا نشد.

━━━━━━━━━━━━━━
"""
        )


        print(
            "📭 No new news"
        )



    print(
        f"🎉 Finished | New news: {new_count}"
    )



if __name__ == "__main__":

    asyncio.run(main())