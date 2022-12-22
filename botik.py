import telebot
import os
from telebot import types

token = '5939425093:AAHO93Zrq_Yi_HNpvulLq024C9ow_h0jYmM'


bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Понедельник1")
    btn2 = types.KeyboardButton("Вторник1")
    btn3 = types.KeyboardButton("Среда1")
    btn4 = types.KeyboardButton("Четверг1")
    btn5 = types.KeyboardButton("Пятница1")
    btn6 = types.KeyboardButton("Вся Неделя 1")
    btn7 = types.KeyboardButton("Сменить Неделю")
    btn8 = types.KeyboardButton("Help")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
    bot.send_message(message.chat.id,
                     text="Здравствуйте, {0.first_name}! Я умею выводить рассписание группы (BIN2201).".format(
                         message.from_user), reply_markup=markup)
    bot.send_message(message.chat.id,
                     text="Уважаемый {0.first_name}! Для более подробной информации о работе со мной пишите /help или же используйте плитки автоматических запросов!".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,
                     ' /Сменить Неделю 1 - переключить неделю на четную \n /Сменить Неделю переключить неделю на нечетную \n /mtuci - Сайт университета \n Далее запросы выбираются спомощью плиток, что достаточно удобно. Если у вас пропали плитки просто свичните недели. Приятного пользования, также не забывайте проверять актуальность рассписания на сайте: https://mtuci.ru/')


@bot.message_handler(commands=['mtuci'])
def mtuci(message):
    bot.send_message(message.chat.id, 'Держите вашу ссылочку: https://mtuci.ru/')


@bot.message_handler(commands=['Сменить Неделю'])
def Switch_Week(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Понедельник")
    btn2 = types.KeyboardButton("Вторник")
    btn3 = types.KeyboardButton("Среда")
    btn4 = types.KeyboardButton("Четверг")
    btn5 = types.KeyboardButton("Пятница")
    btn6 = types.KeyboardButton("Вся Неделя")
    btn7 = types.KeyboardButton("Сменить Неделю 1")
    btn8 = types.KeyboardButton("Help")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
    bot.send_message(message.chat.id, text="Уважаемый {0.first_name}! Вы переключили кнопки на нечетную неделю!".format(
        message.from_user), reply_markup=markup)


@bot.message_handler(commands=['Switch_Week_even'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Понедельник1")
    btn2 = types.KeyboardButton("Вторник1")
    btn3 = types.KeyboardButton("Среда1")
    btn4 = types.KeyboardButton("Четверг1")
    btn5 = types.KeyboardButton("Пятница1")
    btn6 = types.KeyboardButton("Вся Неделя 1")
    btn7 = types.KeyboardButton("Сменить Неделю")
    btn8 = types.KeyboardButton("Help")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
    bot.send_message(message.chat.id,
                     text="Уважаемый {0.first_name}! Вы переключили кнопки на четную неделю!".format(message.from_user),
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "Сменить Неделю"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Понедельник")
        btn2 = types.KeyboardButton("Вторник")
        btn3 = types.KeyboardButton("Среда")
        btn4 = types.KeyboardButton("Четверг")
        btn5 = types.KeyboardButton("Пятница")
        btn6 = types.KeyboardButton("Вся Неделя")
        btn7 = types.KeyboardButton("Сменить Неделю 1")
        btn8 = types.KeyboardButton("Help")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.chat.id,
                         text="Уважаемый {0.first_name}! Вы переключили кнопки на нечетную неделю!".format(
                             message.from_user), reply_markup=markup)

    elif (message.text == "Понедельник"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Понедельник")
        btn2 = types.KeyboardButton("Вторник")
        btn3 = types.KeyboardButton("Среда")
        btn4 = types.KeyboardButton("Четверг")
        btn5 = types.KeyboardButton("Пятница")
        btn6 = types.KeyboardButton("Вся Неделя")
        btn7 = types.KeyboardButton("Сменить Неделю 1")
        btn8 = types.KeyboardButton("Help")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.chat.id, text="Нечетный Понидельник".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id,
                         text="Предмет | Кабинет | Время | Преподаватель \n Выш.математика(л) | Н-526 | 9:30 | Пискарев С.И \n ВВИТ(пр) | Н-324 | 11:20 | Колесников О.В. \n ВВИТ(пр) | Н-324 | 13:10 | Колесников О.В.),".format(
                             message.from_user), reply_markup=markup)

    elif (message.text == "Вторник"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Понедельник")
        btn2 = types.KeyboardButton("Вторник")
        btn3 = types.KeyboardButton("Среда")
        btn4 = types.KeyboardButton("Четверг")
        btn5 = types.KeyboardButton("Пятница")
        btn6 = types.KeyboardButton("Вся Неделя")
        btn7 = types.KeyboardButton("Сменить Неделю 1")
        btn8 = types.KeyboardButton("Help")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.chat.id, text="Нечетный Вторник".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id,
                         text="Предмет | Кабинет | Время | Преподаватель \n Выш.математика(пр) | Н-526 | 9:30 | Пискарев С.И \n Физкультура(пр) | Н-С/Зал-2 | 11:20 | Волохова С.В. \n Иностранный язык(пр) | Н-420 | 13:10 | Мальцева С.Н.".format(
                             message.from_user), reply_markup=markup)
    elif (message.text == "Среда"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Понедельник")
        btn2 = types.KeyboardButton("Вторник")
        btn3 = types.KeyboardButton("Среда")
        btn4 = types.KeyboardButton("Четверг")
        btn5 = types.KeyboardButton("Пятница")
        btn6 = types.KeyboardButton("Вся Неделя")
        btn7 = types.KeyboardButton("Сменить Неделю 1")
        btn8 = types.KeyboardButton("Help")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.chat.id, text="Нечетная Среда".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id,
                         text="Предмет | Кабинет | Время | Преподаватель \n Русский язык(пр) | Н-310 | 13:10 | Горшкова Д.И. \n Физика(л) | Н-347 | 15:25 | Карпов И.А.\n  ".format(
                             message.from_user), reply_markup=markup)

    elif (message.text == "Четверг"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Понедельник")
        btn2 = types.KeyboardButton("Вторник")
        btn3 = types.KeyboardButton("Среда")
        btn4 = types.KeyboardButton("Четверг")
        btn5 = types.KeyboardButton("Пятница")
        btn6 = types.KeyboardButton("Вся Неделя")
        btn7 = types.KeyboardButton("Сменить Неделю 1")
        btn8 = types.KeyboardButton("Help")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.chat.id, text="Нечетная Четверг".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id,
                         text="Предмет | Кабинет | Время | Преподаватель \n Русский язык(л) | Н-514 | 11:20 | Горшкова Д.И. \n История(пр) | Н-424 | 13:10 | Скляр Л.Н. \n  ".format(
                             message.from_user), reply_markup=markup)

    elif (message.text == "Пятница"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Понедельник")
        btn2 = types.KeyboardButton("Вторник")
        btn3 = types.KeyboardButton("Среда")
        btn4 = types.KeyboardButton("Четверг")
        btn5 = types.KeyboardButton("Пятница")
        btn6 = types.KeyboardButton("Вся Неделя")
        btn7 = types.KeyboardButton("Сменить Неделю 1")
        btn8 = types.KeyboardButton("Help")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.chat.id, text="Нечетная Пятница".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id,
                         text="Предмет | Кабинет | Время | Преподаватель \n Физика(лаб) | Н-342 | 9:30 | Тимошина М.И.\n 'Физкультура(пр) | Н-С/Зал-2 | 11:20 | Волохова С.В. \n  ".format(
                             message.from_user), reply_markup=markup)

    elif (message.text == "Вся Неделя"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Понедельник")
        btn2 = types.KeyboardButton("Вторник")
        btn3 = types.KeyboardButton("Среда")
        btn4 = types.KeyboardButton("Четверг")
        btn5 = types.KeyboardButton("Пятница")
        btn6 = types.KeyboardButton("Вся Неделя")
        btn7 = types.KeyboardButton("Сменить Неделю 1")
        btn8 = types.KeyboardButton("Help")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.chat.id, text="Нечетный Понидельник".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id,
                         text="Предмет | Кабинет | Время | Преподаватель \n Выш.математика(л) | Н-526 | 9:30 | Пискарев С.И \n ВВИТ(пр) | Н-324 | 11:20 | Колесников О.В. \n ВВИТ(пр) | Н-324 | 13:10 | Колесников О.В.),".format(
                             message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id, text="Нечетный Вторник".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id,
                         text="Предмет | Кабинет | Время | Преподаватель \n Выш.математика(пр) | Н-526 | 9:30 | Пискарев С.И \n Физкультура(пр) | Н-С/Зал-2 | 11:20 \n Иностранный язык(пр) | Н-420 | 13:10 ".format(
                             message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id, text="Нечетная Среда".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id,
                         text="Предмет | Кабинет | Время | Преподаватель \n Русский язык(пр) | Н-310 | 13:10 | Горшкова Д.И. \n Физика(л) | Н-347 | 15:25 | Карпов И.А.\n  ".format(
                             message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id, text="Нечетная Четверг".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id,
                         text="Предмет | Кабинет | Время | Преподаватель \n Русский язык(л) | Н-514 | 11:20 | Горшкова Д.И. \n История(пр) | Н-424 | 13:10 | Скляр Л.Н. \n  ".format(
                             message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id, text="Нечетная Пятница".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id,
                         text="Предмет | Кабинет | Время | Преподаватель \n Физика(лаб) | Н-342 | 9:30 | Тимошина М.И.\n 'Физкультура(пр) | Н-С/Зал-2 | 11:20 | Волохова С.В. \n  ".format(
                             message.from_user), reply_markup=markup)

    elif (message.text == "Help"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Понедельник")
        btn2 = types.KeyboardButton("Вторник")
        btn3 = types.KeyboardButton("Среда")
        btn4 = types.KeyboardButton("Четверг")
        btn5 = types.KeyboardButton("Пятница")
        btn6 = types.KeyboardButton("Вся Неделя")
        btn7 = types.KeyboardButton("Сменить Неделю 1")
        btn8 = types.KeyboardButton("Help")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.chat.id, text="Ок".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id,
                         ' /Switch_Week_even - переключить неделю на четную \n /Switch_Week переключить неделю на нечетную \n /mtuci - Сайт университета \n Далее запросы выбираются спомощью плиток, что достаточно удобно. Если у вас пропали плитки просто свичните недели. Приятного пользования, также не забывайте проверять актуальность рассписания на сайте: https://mtuci.ru/')


    elif (message.text == "Понедельник1"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Понедельник")
        btn2 = types.KeyboardButton("Вторник")
        btn3 = types.KeyboardButton("Среда")
        btn4 = types.KeyboardButton("Четверг")
        btn5 = types.KeyboardButton("Пятница")
        btn6 = types.KeyboardButton("Вся Неделя")
        btn7 = types.KeyboardButton("Сменить Неделю 1")
        btn8 = types.KeyboardButton("Help")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.chat.id, text="Четный Понидельник".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id,
                         text="Предмет | Кабинет | Время | Преподаватель \n Физика(л) | Н-226 | 9:30 | Карпов И.А. \n Выш.математика(л) | Н-514 | 11:20 | Пискарев С.И \n Иностранный язык(пр) | Н-328 | 13:10 | Мальцева С.Н. \n История(пр) | Н-401 | 15:25 | Скляр Л.Н.".format(
                             message.from_user), reply_markup=markup)

    elif (message.text == "Среда1"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Понедельник")
        btn2 = types.KeyboardButton("Вторник")
        btn3 = types.KeyboardButton("Среда")
        btn4 = types.KeyboardButton("Четверг")
        btn5 = types.KeyboardButton("Пятница")
        btn6 = types.KeyboardButton("Вся Неделя")
        btn7 = types.KeyboardButton("Сменить Неделю 1")
        btn8 = types.KeyboardButton("Help")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.chat.id, text="Четная Среда".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id, text="Предмет | Кабинет | Время | Преподаватель \n ВВИТ(пр) | H-515 | 9:30 \n Физика(пр) | Н-515 | 11:20 | Колесников О.В. \n ВВИТ(пр) | А-222 | 13:10 | Колесников О.В.),".format( message.from_user), reply_markup=markup)

    elif (message.text == "Вторник1"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Понедельник")
        btn2 = types.KeyboardButton("Вторник")
        btn3 = types.KeyboardButton("Среда")
        btn4 = types.KeyboardButton("Четверг")
        btn5 = types.KeyboardButton("Пятница")
        btn6 = types.KeyboardButton("Вся Неделя")
        btn7 = types.KeyboardButton("Сменить Неделю 1")
        btn8 = types.KeyboardButton("Help")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.chat.id, text="Четный Вторник".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id,
                 text="Предмет | Кабинет | Время | Преподаватель \n Выш.математика(пр) | Н-515 | 9:30 | Пискарев С.И \n Физкультура(пр) | Н-С/Зал-2 | 11:20 | Волохова С.В. \n ВВИТ(лаб) | Н-515 | 13:10 | Воронкова М.Н.".format(
                     message.from_user), reply_markup=markup)

    elif (message.text == "Четверг1"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Понедельник")
        btn2 = types.KeyboardButton("Вторник")
        btn3 = types.KeyboardButton("Среда")
        btn4 = types.KeyboardButton("Четверг")
        btn5 = types.KeyboardButton("Пятница")
        btn6 = types.KeyboardButton("Вся Неделя")
        btn7 = types.KeyboardButton("Сменить Неделю 1")
        btn8 = types.KeyboardButton("Help")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.chat.id, text="Четный Четверг".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id,
                 text="Предмет | Кабинет | Время | Преподаватель \n Физика(пр) | Н-515 | 11:20 | Оборотов В.А. \n 'Физкультура(пр) | Н-С/Зал-2 | 13:10 | Волохова С.В. \n История(Л) | Н-526 | 15:25 | Скляр Л.Н.".format(
                     message.from_user), reply_markup=markup)

    elif (message.text == "Пятница1"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Понедельник")
        btn2 = types.KeyboardButton("Вторник")
        btn3 = types.KeyboardButton("Среда")
        btn4 = types.KeyboardButton("Четверг")
        btn5 = types.KeyboardButton("Пятница")
        btn6 = types.KeyboardButton("Вся Неделя")
        btn7 = types.KeyboardButton("Сменить Неделю 1")
        btn8 = types.KeyboardButton("Help")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.chat.id, text="Четная Пятница".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id, text="Предмет | Кабинет | Время | Преподаватель \n Нет пар".format(message.from_user),
                 reply_markup=markup)

    elif (message.text == "Вся Неделя 1"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Понедельник")
        btn2 = types.KeyboardButton("Вторник")
        btn3 = types.KeyboardButton("Среда")
        btn4 = types.KeyboardButton("Четверг")
        btn5 = types.KeyboardButton("Пятница")
        btn6 = types.KeyboardButton("Вся Неделя")
        btn7 = types.KeyboardButton("Сменить Неделю 1")
        btn8 = types.KeyboardButton("Help")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.chat.id, text="Нечетный Понидельник".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id,
                 text="Предмет | Кабинет | Время | Преподаватель \n Физика(л) | Н-226 | 9:30 | Карпов И.А. \n Выш.математика(л) | Н-514 | 11:20 | Пискарев С.И \n Иностранный язык(пр) | Н-328 | 13:10 | Мальцева С.Н. \n История(пр) | Н-401 | 15:25 | Скляр Л.Н.".format(
                     message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id, text="Четный Вторник".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id,
                 text="Предмет | Кабинет | Время | Преподаватель \n Выш.математика(пр) | Н-515 | 9:30 | Пискарев С.И \n Физкультура(пр) | Н-С/Зал-2 | 11:20 | Волохова С.В. \n ВВИТ(лаб) | Н-515 | 13:10 | Воронкова М.Н.".format(
                     message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id, text="Четная Среда".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id,
                 text="Предмет | Кабинет | Время | Преподаватель \n ВВИТ(пр) | H-515 | 9:30 \n Физика(пр) | Н-515 | 11:20 | Колесников О.В. \n ВВИТ(пр) | А-222 | 13:10 | Колесников О.В.),".format(
                     message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id, text="Четный Четверг".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id,
                 text="Предмет | Кабинет | Время | Преподаватель \n Физика(пр) | Н-515 | 11:20 | Оборотов В.А. \n 'Физкультура(пр) | Н-С/Зал-2 | 13:10 | Волохова С.В. \n История(Л) | Н-526 | 15:25 | Скляр Л.Н.".format(
                     message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id, text="Четная Пятница".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id, text="Предмет | Кабинет | Время | Преподаватель \n Нет пар".format(message.from_user),
                 reply_markup=markup)

    elif (message.text == "Сменить Неделю 1"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Понедельник1")
        btn2 = types.KeyboardButton("Вторник1")
        btn3 = types.KeyboardButton("Среда1")
        btn4 = types.KeyboardButton("Четверг1")
        btn5 = types.KeyboardButton("Пятница1")
        btn6 = types.KeyboardButton("Вся Неделя 1")
        btn7 = types.KeyboardButton("Сменить Неделю")
        btn8 = types.KeyboardButton("Help")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.chat.id,
                 text="Уважаемый {0.first_name}! Вы переключили кнопки на четную неделю!".format(message.from_user),
                 reply_markup=markup)

    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")




bot.infinity_polling()