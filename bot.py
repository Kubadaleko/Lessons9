import telebot
import random
import time
import json

token = 'Ваш token'

bot = telebot.TeleBot(token)

number = 0

with open('horoscope.json', 'r', encoding='utf-8') as horo:
    some_dict = json.load(horo)
    print(some_dict)


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = telebot.types.KeyboardButton('Рандомное число')
    item2 = telebot.types.KeyboardButton('Кинуть кость')
    item3 = telebot.types.KeyboardButton('Как дела?')
    # item4 = telebot.types.KeyboardButton('Напоминалка')
    item5 = telebot.types.KeyboardButton('Загадай число')
    item6 = telebot.types.KeyboardButton('Знак зодиака')
    item7 = telebot.types.KeyboardButton('Ответь на вопрос?')

    markup.add(item1, item2, item3, item5, item6, item7)

    bot.send_message(message.chat.id,
                     'Добро пожаловать! Выберите нужный вам пункт меню: ',
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == 'отлично':
        bot.send_message(message.chat.id, 'Я рад за тебя')
    elif message.text.lower() == 'плохо':
        bot.send_message(message.chat.id, 'Что случилось?')
    elif message.text.lower() == 'знак зодиака':
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = telebot.types.KeyboardButton('Овен')
        item2 = telebot.types.KeyboardButton('Телец')
        item3 = telebot.types.KeyboardButton('Близнецы')
        item4 = telebot.types.KeyboardButton('Рак')
        item5 = telebot.types.KeyboardButton('Лев')
        item6 = telebot.types.KeyboardButton('Козерог')
        item7 = telebot.types.KeyboardButton('Весы')
        item8 = telebot.types.KeyboardButton('Скорпион')
        item9 = telebot.types.KeyboardButton('Водолей')
        item10 = telebot.types.KeyboardButton('Стрелец')
        item11 = telebot.types.KeyboardButton('Дева')
        item12 = telebot.types.KeyboardButton('Рыбы')
        markup.add(item1, item2, item3, item4, item5, item6, item7, item8,
                   item9, item10, item11, item12)
        bot.send_message(message.chat.id,
                         'Жмакни на кнопку',
                         reply_markup=markup)
        bot.register_next_step_handler(message, horoscope)

    elif message.text.lower() == 'загадай число':
        global number
        number = random.randint(1, 10)
        bot.send_message(message.chat.id, 'Ок, загадал, от 1 до 10')
        bot.send_message(message.chat.id, 'Давай отгадывай!;)')
        bot.register_next_step_handler(message, think_of)

    elif message.text.lower() == 'как дела?':
        some_list = [
            'Хорошо', 'Плохо', 'Так себе', 'Отлично', 'А сам как думаешь? ',
            'Пока не родила'
        ]
        n = random.randint(0, len(some_list))
        bot.send_message(message.chat.id, some_list[n - 1])
    elif message.text.lower() == 'ответь на вопрос?':
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, 'Итак, Вы в игре')
        item1 = telebot.types.KeyboardButton('1')
        item2 = telebot.types.KeyboardButton('2')
        item3 = telebot.types.KeyboardButton('3')
        markup.add(item1, item2, item3)
        bot.send_message(message.chat.id,
                         'Выбирайте номер вопроса: ',
                         reply_markup=markup)
        bot.register_next_step_handler(message, question)

        # markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        # bot.send_message(message.chat.id, 'Итак, Вы в игре')
        # bot.send_message(message.chat.id, 'Вопрос!')
        # bot.send_message(
        #     message.chat.id,
        #     'Какой головной убор был во время бала на Татьяне Лариной, героине романа «Евгений Онегин»?'
        # )
        # item1 = telebot.types.KeyboardButton('Малиновый берет')
        # item2 = telebot.types.KeyboardButton('Кислотная кепка')
        # item3 = telebot.types.KeyboardButton('Шапка ушанка')
        # item4 = telebot.types.KeyboardButton('Черпак')
        # markup.add(item1, item2, item3, item4)
        # bot.send_message(message.chat.id, 'Ваш ответ?', reply_markup=markup)
        # bot.register_next_step_handler(message, game)

    elif message.text.lower() == 'рандомное число':
        bot.send_message(message.chat.id, str(random.randint(1, 100)))
    elif message.text.lower() == 'кинуть кость':
        bot.send_message(message.chat.id, str(random.randint(1, 7)))
    # elif message.text.lower() == 'напоминалка':
    #     bot.send_message(message.chat.id, 'Введите время для будильника')
    #     bot.register_next_step_handler(message, alarm)
    else:
        bot.send_message(message.chat.id,
                         'Я пока не умею отвечать на данное сообщение!')


# def alarm(message):
#     bot.send_message(message.chat.id, 'Включил напоминалку')


#     global time
#     time = message
#     global chat_id
#     chat_id = message.chat.id
#
# bot.send_message(chat_id)
@bot.message_handler(content_types=['text'])
def think_of(message):
    if message.text.lower() != f'{number}':
        bot.send_message(message.chat.id, 'Неа')
        bot.register_next_step_handler(message, think_of)
    else:
        bot.send_message(message.chat.id, 'Угадал!')
        welcome(message)


@bot.message_handler(content_types=['text'])
def horoscope(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item13 = telebot.types.KeyboardButton('Пожалуй хватит!')
    item1 = telebot.types.KeyboardButton('Овен')
    item2 = telebot.types.KeyboardButton('Телец')
    item3 = telebot.types.KeyboardButton('Близнецы')
    item4 = telebot.types.KeyboardButton('Рак')
    item5 = telebot.types.KeyboardButton('Лев')
    item6 = telebot.types.KeyboardButton('Козерог')
    item7 = telebot.types.KeyboardButton('Весы')
    item8 = telebot.types.KeyboardButton('Скорпион')
    item9 = telebot.types.KeyboardButton('Водолей')
    item10 = telebot.types.KeyboardButton('Стрелец')
    item11 = telebot.types.KeyboardButton('Дева')
    item12 = telebot.types.KeyboardButton('Рыбы')
    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9,
               item10, item11, item12, item13)
    if message.text != 'Пожалуй хватит!':
        bot.send_message(message.chat.id,
                         some_dict[message.text],
                         reply_markup=markup)
        bot.register_next_step_handler(message, horoscope)
    else:
        welcome(message)


@bot.message_handler(content_types=['text'])
def question_num(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot.send_message(message.chat.id, 'Итак, Вы в игре')
    item1 = telebot.types.KeyboardButton('1')
    item2 = telebot.types.KeyboardButton('2')
    item3 = telebot.types.KeyboardButton('3')
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id,
                     'Выбирайте номер вопроса: ',
                     reply_markup=markup)
    bot.register_next_step_handler(message, question)


@bot.message_handler(content_types=['text'])
def game(message):
    if message.text == 'Малиновый берет':
        bot.send_message(message.chat.id, 'Отлично!')
        question_num(message)
    if message.text == 'Северного оленя':
        bot.send_message(message.chat.id, 'Отлично!')
        question_num(message)
    if message.text == 'Сахарная вата':
        bot.send_message(message.chat.id, 'Отлично!')
        question_num(message)
    elif message.text != 'Малиновый берет' and message.text != 'Северного оленя' and message.text != 'Сахарная вата':
        bot.send_message(message.chat.id, 'Не верно! Вы проиграли.')
        welcome(message)


@bot.message_handler(content_types=['text'])
def question(message):
    if message.text.lower() == '1':
        bot.send_message(
            message.chat.id,
            'Какой головной убор был во время бала на Татьяне Лариной, героине романа «Евгений Онегин»?'
        )
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = telebot.types.KeyboardButton('Малиновый берет')
        item2 = telebot.types.KeyboardButton('Кислотная кепка')
        item3 = telebot.types.KeyboardButton('Шапка ушанка')
        item4 = telebot.types.KeyboardButton('Черпак')
        markup.add(item1, item2, item3, item4)
        bot.send_message(message.chat.id, 'Ваш ответ?', reply_markup=markup)
        bot.register_next_step_handler(message, game)

    if message.text.lower() == '2':
        bot.send_message(
            message.chat.id,
            'Чьим детёнышем был пыжик, из меха которого в Советском Союзе делали зимние шапки?'
        )
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = telebot.types.KeyboardButton('Северного оленя')
        item2 = telebot.types.KeyboardButton('Колючего ежа')
        item3 = telebot.types.KeyboardButton('Черепахи')
        item4 = telebot.types.KeyboardButton('Пыжика')
        markup.add(item1, item2, item3, item4)
        bot.send_message(message.chat.id, 'Ваш ответ?', reply_markup=markup)
        bot.register_next_step_handler(message, game)

    if message.text.lower() == '3':
        bot.send_message(
            message.chat.id,
            'Какой продукт в разных странах называют папиной бородой и бабушкиными волосами?'
        )
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = telebot.types.KeyboardButton('Малиновый джем')
        item2 = telebot.types.KeyboardButton('Сахарная вата')
        item3 = telebot.types.KeyboardButton('Виноград')
        item4 = telebot.types.KeyboardButton('Пирог с бататом')
        markup.add(item1, item2, item3, item4)
        bot.send_message(message.chat.id, 'Ваш ответ?', reply_markup=markup)
        bot.register_next_step_handler(message, game)


bot.polling(none_stop=True)
