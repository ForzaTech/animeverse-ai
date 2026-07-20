from google import genai
from config import GEMINI_API_KEY


client = genai.Client(
    api_key=GEMINI_API_KEY
)


def generate_anime_analysis(title, summary):

    prompt = f"""
تو AnimeVerse AI هستی؛ یک خبرنگار حرفه‌ای دنیای انیمه، مانگا و مانهوا.

خبر:

عنوان:
{title}

توضیحات:
{summary}


این خبر را به فارسی حرفه‌ای تحلیل کن.


🌸 عنوان خبر

📰 چه اتفاقی افتاده؟

📖 جزئیات مهم

✨ تحلیل AnimeVerse

🎭 حال و هوا

⭐ ارزش دنبال کردن از ۱۰

💫 نظر نهایی AnimeVerse


قوانین:
- فارسی روان بنویس
- ترجمه خشک نباشد
- مثل یک خبرنگار انیمه‌ای صحبت کن
- اطلاعات بی‌اساس نساز
"""


import time


def generate_anime_analysis(title, summary):

    prompt = f"""
تو AnimeVerse AI هستی؛ خبرنگار حرفه‌ای انیمه، مانگا و مانهوا.

عنوان:
{title}

توضیحات:
{summary}

به فارسی بنویس:

🌸 عنوان خبر

📰 چه اتفاقی افتاده؟

📖 جزئیات

✨ تحلیل AnimeVerse

🎭 حال و هوا

⭐ امتیاز از ۱۰

💫 نظر نهایی
"""


    models = [
        "gemini-flash-latest",
        "gemini-2.0-flash"
    ]


    for model_name in models:

        try:

            response = client.models.generate_content(
                model=model_name,
                contents=prompt
            )

            return response.text


        except Exception as e:

            print(
                f"⚠️ مدل {model_name} خطا داد:",
                e
            )

            time.sleep(3)


    return """
⚠️ AnimeVerse AI

فعلاً سرویس تحلیل هوش مصنوعی در دسترس نیست.
"""


    return response.text