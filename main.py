import telebot
import time
from config import token_api
from intro_text import intro_text
import markups as mark
import sqlite3

my_id = "your ID in Telegram" # Ваш айди куда будет приходить сообщения с информацией о юзере и его заявке


def get_info_user(bot, message):  # функция для отправки информации о юзере в личку
    bot.send_message(my_id, message.text + ' '
                     + f'{message.chat.id}' + ' '
                     + f'{message.from_user.first_name}' + ' '
                     + f'{message.from_user.last_name}')


def run_bot():
    bot = telebot.TeleBot(token_api)

    @bot.message_handler(commands=['start'])  # приветственная функция
    def send_welcome(message):
        
        conn = sqlite3.connect('users_manager_bot.db')
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS users(
           userid INT PRIMARY KEY,
           fname TEXT,
           lname TEXT);
        """)
        conn.commit()

        user_info = (f'{message.chat.id}',
                     f'{message.from_user.first_name}',
                     f'{message.from_user.last_name}')

        cur.execute("INSERT OR IGNORE INTO users VALUES(?, ?, ?);", user_info)  # если есть такая запись не записывать
        conn.commit()

        img = open('title.jpg', 'rb')
        bot.send_photo(message.chat.id, img)
        welcome_user = f'Здравствуйте {message.from_user.first_name} {message.from_user.last_name}' + intro_text

        bot.send_message(message.chat.id, welcome_user,
                         reply_markup=mark.main_menu)

    @bot.message_handler(content_types=['text'])
    def send_markup(message):
        if message.text == 'Мне нужна другая программа':
            bot.send_message(message.chat.id, 'Хорошо! Опишите своими словами '
                                              'что должна делать программа и в конце своего описания поставьте символ @ '
                                              '\nчто-бы я понял Вас.', reply_markup=mark.del_markup)
        elif '@' in message.text:
            bot.send_message(message.chat.id, 'Спасибо, с Вами свяжутся в ближайшее время!',
                             reply_markup=mark.del_markup)
            get_info_user(bot, message)

        elif message.text == 'Мне нужен Чат-бот':
            bot.send_message(message.chat.id, 'Хорошо! На сколько вопросов бот должен ответить?',
                             reply_markup=mark.how_ques)

        elif message.text == 'До 10 вопросов':
            bot.send_message(message.chat.id, 'У бота должен быть дополнительный функционал? '
                                              'Например сохранение или обработка данных?',
                             reply_markup=mark.any_func)

        elif message.text == 'От 10 до 20':
            bot.send_message(message.chat.id, 'У бота должен быть дополнительный функционал? '
                                              'Например сохранение или обработка данных?',
                             reply_markup=mark.any_func)

        elif message.text == 'Более 20':
            bot.send_message(message.chat.id, 'У бота должен быть дополнительный функционал? '
                                              'Например сохранение или обработка данных?',
                             reply_markup=mark.any_func)

        elif message.text == 'Будут доп. функции':
            bot.send_message(message.chat.id, f'Благодарим за опрос, Ваша предварительная стоимость 1400 рублей.'
                                              '\nЦена может варьироваться в зависимости от сложности Бота',
                             reply_markup=mark.back_menu)
            get_info_user(bot, message)

        elif message.text == 'Нет сложных функций':
            bot.send_message(message.chat.id, f'Благодарим за опрос, Ваша предварительная стоимость 1100 рублей.'
                                              '\nЦена может варьироваться в зависимости от сложности Бота',
                             reply_markup=mark.back_menu)
            get_info_user(bot, message)

        elif message.text == 'Назад':
            img = open('title.jpg', 'rb')
            bot.send_photo(message.chat.id, img)
            bot.send_message(message.chat.id, intro_text,
                             reply_markup=mark.main_menu)
        else:
            bot.send_message(message.chat.id, 'Я Вас не понял =(')

    while True:  # функция для пулинга
        print('=^.^=' ver 1.0) # информация о статусе бота в коммандной строке 

        try:
            bot.polling(none_stop=True, interval=3, timeout=20)
            print('Этого не должно быть')
        except telebot.apihelper.ApiException:
            print('Проверьте связь и API')
            time.sleep(10)
        except Exception as e:
            print(e)
            time.sleep(60)


if __name__ == '__main__':
    run_bot()
