import telebot
from openai import OpenAI

BOT_TOKEN = '7971673745:AAFZN-6mqlkoc8gi69eN6gJlNGWRcyjrdI8'
bot = telebot.TeleBot(BOT_TOKEN)

# DeepSeek через OpenRouter с новым клиентом
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"
)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "Привет! Напиши, в каком ты настроении, и я подберу фильмы под него 🎬"
    )

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_input = message.text.strip()

    prompt = (
        f"Пользователь чувствует: \"{user_input}\".\n"
        "Предложи 5 фильмов, подходящих под это настроение, с кратким описанием. Ответь по-русски, красиво и понятно."
    )

    try:
        completion = client.chat.completions.create(
            model="deepseek/deepseek-chat-v3-0324:free",
            messages=[{"role": "user", "content": prompt}],
            extra_headers={
                "HTTP-Referer": "https://yourproject.site",  # можешь указать свой сайт
                "X-Title": "TelegramMovieBot"
            }
        )

        reply = completion.choices[0].message.content
        bot.send_message(message.chat.id, reply)

    except Exception as e:
        bot.send_message(message.chat.id, f"Ошибка при запросе к модели: {str(e)}")

bot.polling()
