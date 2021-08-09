import telebot

# --- Main menu ---
main_menu = telebot.types.ReplyKeyboardMarkup(True)
main_menu.row('Мне нужен Чат-бот', 'Мне нужна другая программа')

# ---back menu ---
back_menu = telebot.types.ReplyKeyboardMarkup(True)
back_menu.row('Назад')

# --- Delete markup ---
del_markup = telebot.types.ReplyKeyboardRemove()

# --- questions ---
how_ques = telebot.types.ReplyKeyboardMarkup(True)
how_ques.row('До 10 вопросов', 'От 10 до 20', 'Более 20')

# --- add function ---
any_func = telebot.types.ReplyKeyboardMarkup(True)
any_func.row('Будут доп. функции', 'Нет сложных функций')