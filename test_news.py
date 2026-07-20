from news.anime import get_anime_news


news = get_anime_news()


for item in news:
    print("📰", item["title"])
    print("🔗", item["link"])
    print("----------------")