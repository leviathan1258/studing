import telebot
import time
from telebot import types


bot = telebot.TeleBot("7958430002:AAE12foVhWq1WgfKisUR-ZmD73D9bPoWjAI")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я бот, созданный чтобы помочь людям с проблемами пластика!")
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Поделки!', callback_data = 'handmake'))
    markup.add(types.InlineKeyboardButton("Соритровка отдходов!", callback_data = 'sort'))
    markup.add(types.InlineKeyboardButton("Время разложения отходов!", callback_data = 'time'))
    bot.send_message(message.chat.id, "Вот какую помощь я могу предложить:", reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def buttons(callback):
    if callback.data == 'handmake':
        bot.send_message(callback.message.chat.id, "И так, список поделок которые ты можешь сделать из пластика:")
        time.sleep(1)
        bot.send_message(callback.message.chat.id, "1. Фонтан из бутылок \nhttps://www.youtube.com/watch?v=PdUxcKjG3TQ")
        time.sleep(0.7)
        bot.send_message(callback.message.chat.id, "2. Горшки для цветов! \nhttps://www.youtube.com/watch?v=tUR4INUiZaQ")
        time.sleep(0.7)
        bot.send_message(callback.message.chat.id, "3. Кормушки и скворечники! \nhttps://www.youtube.com/watch?v=cB2W-1h9Jrk")
        
    elif callback.data == 'sort':
        bot.send_message(callback.message.chat.id, "Можно переработать:")
        time.sleep(0.5)
        bot.send_message(callback.message.chat.id, "СТЕКЛО \nДля вторичной переработки подходят стеклянные бутылки, банки из-под разных напитков и продуктов, флаконы из-под парфюмерии и лекарств")
        time.sleep(0.7)
        bot.send_message(callback.message.chat.id, 'МАКУЛАТУРА \nВ макулатуру отправляют ненужные книги, газеты, журналы, тетради, рекламные буклеты. Для переработки подходят альбомы с рисунками акварелью, гуашью, карандашами.\n\n<u>Не примут в макулатуру обои, салфетки, лотки из-под яиц, сигаретные пачки, ламинированную, промасленную и фотобумагу, кальку и чеки из магазина, которые содержат токсичные вещества.</u>', parse_mode="HTML")
        time.sleep(0.7)
        bot.send_message(callback.message.chat.id, "ПЛАСТИК \nМожно отправлять в переработку пластиковые бутылки (кроме емкостей из-под масла), пакеты, контейнеры для еды, предметы домашнего обихода, игрушки. \n\nДругие пластиковые изделия представляют опасность и не подходят для переработки. Это ламинат, трубы, технические емкости с маркировкой PVC, лотки из полистирола (маркировка PS), одноразовая посуда и пластиковая упаковка.")
        time.sleep(0.7)
        bot.send_message(callback.message.chat.id, "МЕТАЛЛ \nСтарую, пришедшую в негодность бытовую технику не отправляют на свалку, а сдают в специальные пункты. Из мелких бытовых предметов отсортировывают и сдают металлическую посуду, инструменты, алюминиевые и жестяные банки из-под напитков и продуктов.")
        time.sleep(0.7)
        bot.send_message(callback.message.chat.id, "Нельзя переработать:")
        time.sleep(0.7)
        bot.send_message(callback.message.chat.id, "Салфетки, бумажные полотенца, чеки, виниловые обои, ламинированная бумага, фотографии, одноразовые бумажные стаканчики, стеклотара, если она битая, керамика, фаянс и хрусталь, энергосберегающие лампы, градусники, батарейки, старая бытовая техника, старая мебель и строительный мусор, Пластиковая тара, <u>кроме чистой упаковки с маркировкой 01, PET, ПЭТ, 02, HDPE, ПЭВП</u>", parse_mode="HTMl")

    elif callback.data == 'time':
        bot.send_message(callback.message.chat.id, "Отходы до 3 лет: \n\nПищевые отходы - до 1 месяца\n Газетная бумага - до 1 года\nКартонные коробки - до 1 года\nБумага - 2 года")
        time.sleep(0.5)
        bot.send_message(callback.message.chat.id, "Отходы до 10 лет: \n\n Доски деревянные - до 10 лет \nЖелезная арматура - до 10 лет \nЖелезные банки - до 10 лет \nСтарая обувь - до 10 лет")
        time.sleep(0.7)
        bot.send_message(callback.message.chat.id, 'Отходы до 100 лет: \n\nОбломки кирпича, бетона- до 100 лет \n\nАвтоаккумуляторы - до 100 лет \nФольга - до 100 лет \nЭлектрические батарейки - до 100 лет ')
        time.sleep(0.7)
        bot.send_message(callback.message.chat.id, "Отходы более 100 лет: \n\nРезиновые покрышки - более 100 лет \тПластиковые бутылки - более 100 лет \nПолиэтиленовые пленки - 200 лет \nАлюминиевые банки - 500 лет")
        time.sleep(0.7)
        bot.send_message(callback.message.chat.id, "Отходы на 1000 лет: \n\nСтекло - 1000 лет")

bot.polling(non_stop=True)
