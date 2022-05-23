# import telebot
# from config import API, TOKEN
# from telebot import types
# from random import *
# import requests


# bot = telebot.TeleBot(TOKEN)
# markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
# markup.row('Искать город', 'Инфо', 'Рандомное число', 'Как дела?')


# @bot.message_handler(commands=['start'])
# def welcome(message):
#     sticker = open('images/sticker.webp', 'rb')
#     bot.send_sticker(message.chat.id, sticker)
    
#     bot.send_message(message.chat.id, 
#                     'Добро пожаловать {0.first_name}! \n Я'
#                     '<b>{1.first_name}</b> Ваш бот'.format(
#                         message.from_user, bot.get_me()),
#                         parse_mode = 'html', reply_markup=markup
#     )

# @bot.message_handler(commands=['Искать город'])
# def welocome(message):
#     msg = f"<b>City:</b>"
#     bot.send_message(message.chat.id, msg, parse_mode='html')


# @bot.message_handler(commands=['geo'])
# def geo(message):
#     keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
#     button_geo = types.KeyboardButton(text='Отправить геолокацию', 
#                                             request_location=True)
#     keyboard.add(button_geo)
#     bot.send_message(message.chat.id, 'Привет! Нажми чтобы отправить геолокацию.',
#                                     reply_markup=keyboard)



# @bot.message_handler(content_types=['location'])
# def location(message):
#     if message.location is not None:
#         print(message.location)
#         print("Широта: %s, Долгота: %s" % (message.location.latitude,
#                                             message.location.longitude))


# @bot.message_handler(content_types=['text'])
# def main(message):
#     if message.chat.type == 'private':
#         if message.text == 'Искать город':
#             msg = f"<b>Назовите город: </b>"
#             bot.send_message(message.chat.id, msg, parse_mode='html')
#         elif message.text == 'Инфо':
#             msg = 'Бот служит для прогноз погоды и геолокации. Создатель: Бекназар'
#             bot.send_message(message.chat.id, msg)
#         elif message.text == 'Рандомное число':
#             bot.send_message(message.chat.id, str(randint(0, 10000)))
#         elif message.text == 'Как дела?':
#             markup = types.InlineKeyboardMarkup(row_width=3)
#             item1 = types.InlineKeyboardButton('Не жалуюсь',callback_data='not bad')
#             item2 = types.InlineKeyboardButton('Просто замечательно :)', 
#                                                 callback_data='good')
#             item3 = types.InlineKeyboardButton('Хочу закрыть глаза и никогда не открывать :(', 
#                                                 callback_data='bad')

#             markup.add(item1, item2, item3)
#             bot.send_message(message.chat.id, 'Просто офигенно! :)', 
#                             reply_markup=markup)


#         else:
#             try:
#                 CITY=message.text
                
#                 URL = f'https://api.openweathermap.org/data/2.5/weather?q={CITY}&units=metric&appid={API}'
#                 response=rewuests.get(url=URL).json()
#                 city_info={
#                     'city':CITY,
#                     'temp':response['main']['temp'],
#                     'humadity':response['main']['humadity'],
#                     'weather':response['wearther'][0]['desscription'],
#                     'pressure':response['main']['pressure'],
#                 }
#                 msg = f"<b><u>{CITY.upper()}</u>\n\nПогода {city_info['weather']}</b>--------------------------------\n🌡 Температура: <b>{city_info['temp']} C</b>\n💨 Ветренность: <b>{city_info['wind']} м/с</b> \n💦 Влажность: <b>{city_info['humadity']}%</b>\n🧬Давление: <b>{city_info['pressure']} hPa</b>"
#             except:
#                 sg1=f'<b>Мы ничего не смогли найти'
#                 bot.send_message(message.chat.id,msg1,parse_mode='html')



# bot.polling(none_stop=True)
import telebot
from yaml import parse
from config import API, TOKEN
from telebot import types
from random import *
import requests


bot = telebot.TeleBot(TOKEN)
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup.row('Редми', 'Айфон', 'Самсунг', 'Инфо')


@bot.message_handler(commands=['start'])
def welcome(message):
    sticker = open('images/sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sticker)
    
    bot.send_message(message.chat.id, 
                    'Добро пожаловать {0.first_name}! \n Я'
                    '<b>{1.first_name}</b> Ваш бот.Какой телефон хотите?'.format(
                        message.from_user, bot.get_me()),
                        parse_mode = 'html', reply_markup=markup
    )



@bot.message_handler(content_types=['location'])
def location(message):
    if message.location is not None:
        print(message.location)
        print("Широта: %s, Долгота: %s" % (message.location.latitude,
                                            message.location.longitude))


@bot.message_handler(content_types=['text'])
def main(message):
    if message.chat.type == 'private':
        if message.text == message.text == 'Айфон':
            markup = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton('IPhone SE',callback_data='item4')
            item2 = types.InlineKeyboardButton('IPhone 13 Pro Max', 
                                                callback_data='item5')
            item3 = types.InlineKeyboardButton('IPhone 12 Pro', 
                                                callback_data='item6')

            markup.add(item1, item2, item3)
            bot.send_message(message.chat.id, 'У нас в наличии есть ниже указанные модели.Выберите модель, пожалуйста!', 
                            reply_markup=markup)
        elif message.text == 'Редми':
            markup = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton('Mi 6',callback_data='not bad')
            item2 = types.InlineKeyboardButton('Mi 8', 
                                                callback_data='good')
            item3 = types.InlineKeyboardButton('Mi 6x', 
                                                callback_data='bad')

            markup.add(item1, item2, item3)
            bot.send_message(message.chat.id, 'У нас в наличии есть ниже указанные модели.Выберите модель, пожалуйста!', 
                            reply_markup=markup)
        elif message.text == 'Инфо':
            msg = 'Бот служит для выбора смартфона.'
            bot.send_message(message.chat.id, msg)

        elif message.text == 'Самсунг':
            markup = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton('Galaxy S22',callback_data='item7')
            item2 = types.InlineKeyboardButton('Galaxy S22 ulra', 
                                                callback_data='item8')
            item3 = types.InlineKeyboardButton('Galax A53', 
                                                callback_data='item9')

            markup.add(item1, item2, item3)
            bot.send_message(message.chat.id, 'У нас в наличии есть ниже указанные модели.Выберите модель, пожалуйста!', 
                            reply_markup=markup)

        else:
            try:
                CITY = message.text
                URL = f'https://api.openweathermap.org/data/2.5/weather?q={CITY}&units=metric&appid={API}'
                response = requests.get(url=URL).json()
                city_info = {
                    'city': CITY,
                    'temp': response['main']['temp'],
                    'humidity': response['main']['humidity'],
                    'weather': response['weather'][0]['description'],
                    'wind': response['wind']['speed'],
                    'pressure': response['main']['pressure'],
                }
                msg = f"<b><u>{CITY.upper()}</u>\n\nWeather is{city_info['weather']}</b>\n------------------------------------\n🌡 Температура: <b>{city_info['temp']} C</b>\n💨 Ветренность: <b>{city_info['wind']} m/s</b>\n💦 Влажность: <b>{city_info['humidity']} %</b>\n🧬 Давление: <b>{city_info['pressure']} hPa</b>"
                bot.send_message(message.chat.id, msg, parse_mode='html')
            except:
                msg1 = f"<b>🙅‍♂️ Nothing found try again</b>"
                bot.send_message(message.chat.id, msg1, parse_mode='html')

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    try:
        if call.message:
            if call.data =='good':
                bot.send_message(call.message.chat.id,'''Основные характеристики Xiaomi Mi 8

    SoC Qualcomm Snapdragon 845, 8 ядер (4 × Kryo 385 @2,8 ГГц + 4 × Kryo 385 @1,8 ГГц)
    GPU Adreno 630.
    Операционная система Android 8.1, MIUI 10.
    Сенсорный дисплей AMOLED 6,21″, 2248×1080 (18,7:9), 402 ppi.
    Оперативная память (RAM) 6 ГБ, внутренняя память 64/128/256 ГБ''')
            elif call.data=='bad':
                bot.send_message(call.message.chat.id,'''Каковы характеристики Xiaomi Mi 6x?

    Экран: 5.99" LCD IPS.
    Разрешение: 1080 x 2160 px · FHD+
    RAM: 4GB - 6GB.
    Хранение: 64GB - 128GB.
    Процессора: Qualcomm Snapdragon 660 MSM8976 Plus.''')
            elif call.data=='not bad':
                bot.send_message(call.message.chat.id,'''Полные характеристики Xiaomi Mi 6

    Дисплей: 5.15 дюймов, Full HD, 600 Нит
    Процессор: Qualcomm Snapdragon 835, 8 ядер, 2.45 ГГц
    Графика: Adreno 540 GPU.
    ОЗУ: 6 Гб LPDDR4.
    Флеш-память: 64/128 Гб UFS.
    Основная камера: два сенсора по 12 Мп, OIS, 2-кратный оптический зум
    Фронтальная камера: 8 Мп''')
  

    
        
            elif call.data =='item1':
                bot.send_message(call.message.chat.id,'''Основные характеристики nokia Mi 8

    SoC Qualcomm Snapdragon 845, 8 ядер (4 × Kryo 385 @2,8 ГГц + 4 × Kryo 385 @1,8 ГГц)
    GPU Adreno 630.
    Операционная система Android 8.1, MIUI 10.
    Сенсорный дисплей AMOLED 6,21″, 2248×1080 (18,7:9), 402 ppi.
    Оперативная память (RAM) 6 ГБ, внутренняя память 64/128/256 ГБ''')
            elif call.data=='item2':
                bot.send_message(call.message.chat.id,'''Каковы характеристики Xiaomi Mi 6x?

    Экран: 5.99" LCD IPS.
    Разрешение: 1080 x 2160 px · FHD+
    RAM: 4GB - 6GB.
    Хранение: 64GB - 128GB.
    Процессора: Qualcomm Snapdragon 660 MSM8976 Plus.''')
            elif call.data=='item3':
                bot.send_message(call.message.chat.id,'''Полные характеристики Xiaomi Mi 6

    Дисплей: 5.15 дюймов, Full HD, 600 Нит
    Процессор: Qualcomm Snapdragon 835, 8 ядер, 2.45 ГГц
    Графика: Adreno 540 GPU.
    ОЗУ: 6 Гб LPDDR4.
    Флеш-память: 64/128 Гб UFS.
    Основная камера: два сенсора по 12 Мп, OIS, 2-кратный оптический зум
    Фронтальная камера: 8 Мп''')
            elif call.data =='item4':
                bot.send_message(call.message.chat.id,'''Характеристики iPhone SE 3
    Дисплей: 4.7 дюймов, IPS LCD;
    Процессор: Apple A15 Bionic;
    Память: 64 ГБ / 128 ГБ / 256 ГБ;
    ОЗУ: 3 ГБ;
    Операционная система: iOS 15.4;
    Порт: Lightning;
    Фронтальная камера: 7 Мп;
    Основная камера: 12 Мп + новые возможности киностилей и HDR 4;''')
            elif call.data=='item5':
                bot.send_message(call.message.chat.id,'''Технические характеристики iPhone 13 Pro Max:

    Габариты: 160,8×78,1×7,65 мм, 238 г
    Дисплей: 6,7", OLED, Super Retina XDR, 2778×1284 , 458 ppi, 120 Гц
    Процессор: 6-ядерный Apple A15 Bionic.
    Память: 6 ГБ ОЗУ, 128/256/512 ГБ или 1 ТБ ПЗУ''')
            elif call.data=='item6':
                bot.send_message(call.message.chat.id,'''Тип   OLED
    Размер   6.7 дюймов
    Разрешение   1284 x 2778 пикселей
    Соотношение сторон   19.5:9
    Плотность пикселей   458 точек на дюйм
    Частота обновления   60 Гц
    Поддержка HDR   Да, Dolby Vision
    Защита дисплея   Ceramic Shield
    Соотношение экрана к корпусу   87.4%
    Особенности   - DCI-P3;''')
            elif call.data =='item7':
                bot.send_message(call.message.chat.id,'''Samsung Galaxy S22 5G смартфон 2022 года выпуска. Его размеры 146 x 70.6 x 7.6 и вес 167 г. Он оснащен Dynamic AMOLED 2X-дисплеем с размером 6.1" дюйма. Разрешение составляет 1080 x 2340 пикселей, плотность пикселей 425 ppi. Для селфи и видеозвонков отвечает Одна предна камера с 10 MP. Для базовых фото и видео доступная Тройная задняя камера 50 MP. Процессор есть Octa-core (1x2.8 GHz Cortex-X2 & 3x2.50 GHz Cortex-A710 & 4x1.7 GHz Cortex-A510) - International Octa-core (1x3.00 GHz Cortex-X2 & 3x2.50 GHz Cortex-A710 & 4x1.80 GHz Cortex-A510) - USA/China и памяти 128GB 8GB RAM, 256GB 8GB RAM. Емкость аккумулятора 3700 mAh. Подробности читайте ниже..''')
            elif call.data=='item8':
                bot.send_message(call.message.chat.id,'''Samsung Galaxy S22 Ultra 5G смартфон 2022 года выпуска. Его размеры 163.3 x 77.9 x 8.9 и вес 228 г. Он оснащен Dynamic AMOLED 2X-дисплеем с размером 6.8" дюйма. Разрешение составляет 1440 x 3088 пикселей, плотность пикселей 500 ppi.''')
            elif call.data=='item9':
                bot.send_message(call.message.chat.id,'''Для селфи и видеозвонков отвечает Одна предна камера с 32 MP. Для базовых фото и видео доступная Четверная задняя камера 64 MP. Процессор есть Octa-core (2x2.4 GHz Cortex-A78 & 6x2.0 GHz Cortex-A55) и памяти 128GB 4GB RAM, 128GB 6GB RAM, 128GB 8GB RAM, 256GB 6GB RAM, 256GB 8GB RAM. Емкость аккумулятора 5000 mAh.''')
    except Exception as e:
        print(repr(e))
    

bot.polling(none_stop=True)



































































































