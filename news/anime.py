import feedparser


ANIME_NEWS_RSS = "https://feeds.feedburner.com/animenewsnetwork"


def get_anime_news():

    feed = feedparser.parse(ANIME_NEWS_RSS)

    news_list = []


    for item in feed.entries[:5]:

        news = {

            "title": item.get(
                "title",
                "بدون عنوان"
            ),

            "link": item.get(
                "link",
                ""
            ),

            "summary": item.get(
                "summary",
                ""
            ),

            "type": "anime"

        }


        news_list.append(news)


    return news_list



if __name__ == "__main__":


    news = get_anime_news()


    print(
        "تعداد خبرها:",
        len(news)
    )


    for item in news:

        print(
            "\n📰",
            item["title"]
        )

        print(
            "📌 دسته:",
            item["type"]
        )

        print(
            "🔗",
            item["link"]
        )

        print(
            "📝",
            item["summary"][:100]
        )