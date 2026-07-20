import feedparser


MANGA_FEEDS = [

    "https://www.animenewsnetwork.com/newsfeed.xml",

    "https://www.animenewsnetwork.com/all/rss.xml",

    "https://myanimelist.net/rss/news.xml",

    "https://animehunch.com/feed/",

    "https://www.animenewsnetwork.com/news/rss.xml"

]


def get_manga_news():

    news_list = []


    manga_words = [

        "manga",
        "manhwa",
        "comic",
        "chapter",
        "volume",
        "serialization",
        "serialized",
        "author",
        "mangaka",
        "shonen",
        "shojo"

    ]



    for url in MANGA_FEEDS:


        try:

            feed = feedparser.parse(url)


            for item in feed.entries[:10]:


                title = item.get(
                    "title",
                    ""
                )


                summary = item.get(
                    "summary",
                    ""
                )


                text = (
                    title + " " + summary
                ).lower()



                if any(
                    word in text
                    for word in manga_words
                ):


                    news_list.append(

                        {

                            "title": title,

                            "summary": summary,

                            "link": item.get(
                                "link",
                                ""
                            ),

                            "type": "manga"

                        }

                    )



                if len(news_list) >= 5:

                    return news_list



        except Exception as e:

            print(
                "Feed error:",
                url,
                e
            )



    return news_list




if __name__ == "__main__":


    news = get_manga_news()


    print(
        "تعداد خبرهای مانگا:",
        len(news)
    )


    for item in news:


        print(
            "\n📚",
            item["title"]
        )

        print(
            "📌",
            item["type"]
        )

        print(
            "🔗",
            item["link"]
        )