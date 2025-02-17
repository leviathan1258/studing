import telebot
import random
import os
from telebot.types import ReactionTypeEmoji
from telebot import custom_filters

bot = telebot.TeleBot("7958430002:AAE12foVhWq1WgfKisUR-ZmD73D9bPoWjAI")

@bot.message_handler(commands=['mem'])
def send_mem(message):
    img_name = random.choice(os.listdir("images"))
    with open(f'images/{img_name}', 'rb') as f:  
        bot.send_photo(message.chat.id, f) 

@bot.message_handler(commands=['amem'])
def send_mem(message):
    img_name = random.choice(os.listdir("images/animals"))
    with open(f'images/animals/{img_name}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=['pmem'])
def send_mem(message):
    img_name = random.choice(os.listdir("images/people"))
    with open(f'images/people/{img_name}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)

@bot.message_handler(content_types=['photo'])
def send_reaction(message):
    emo = "\U0001F525"  #🔥
    bot.set_message_reaction(message.chat.id, message.id, [ReactionTypeEmoji(emo)], is_big=False)

# Check if message starts with @admin tag
@bot.message_handler(text_startswith="@admin")
def start_filter(message):
    bot.send_message(message.chat.id, "Looks like you are calling admin, wait...")

# Check if text is hi or hello
@bot.message_handler(text=['hi','hello'])
def text_filter(message):
    bot.send_message(message.chat.id, "Hi, {name}!".format(name=message.from_user.first_name))

# Do not forget to register filters
bot.add_custom_filter(custom_filters.TextMatchFilter())
bot.add_custom_filter(custom_filters.TextStartsFilter())

bot.polling(non_stop=True)
