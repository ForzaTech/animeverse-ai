from ai.analyzer import analyze_news


text = analyze_news(
    "New anime adaptation announced",
    "A popular manga will receive a TV anime adaptation."
)


print(text)