# manager_bot

Бот с клавиатурой , для приёма заявок в телеграме и обозначения предварительной стоимости услуг. Данные записываем в БД SQLite.
A bot with a keyboard for accepting applications in telegram and indicating the preliminary cost of services. We write the data to the SQLite database.

## Модули 
*в файле **markups.py** обьявлены все клавиатуры для удобства расширения бота. Логика бота и код в **main.py***

*В **config.py** лежит токен бота*

*В **intro_text.py** вводный текст*

*В **title.jpg**  начальная картинка*

## Moduls 
*all keyboards are declared in the **markups.py** file for the convenience of expanding the bot. Bot logic and code in **main.py***

*In **config.py** there is a bot token*

*In **intro_text.py** introductory text*

*In **title.jpg** initial picture*

## Зависимости
Python 3.X

Обязательно установите виртуальное окружение:

1) `python -m venv venv` 

Иначе могут быть проблемы, если установлены другие версии или библиотеки от telethon, Telegrambotapi и пр.

Зависимости в в файле requirements.txt,можно установить с момощью pip:

2) `pip install -r requirements.txt `

## Dependencies
Python 3.X

Be sure to install the virtual environment:

1) `python -m venv venv` 

Otherwise, there may be problems if other versions or libraries from telethon, Telegrambotapi, etc. are installed.

Dependencies in the req.txt file can be installed using pip:

2) `pip install -r req.txt`
 
## Запуск
1) В файле **config.py** прописываем токен бота [(взять можно в BotFather)](https://telegram.me/BotFather)

2) Запускаем `python main.py`

## Run
1) In the **config.py** file we register the bot token [(you can get it in BotFather)](https://telegram.me/BotFather)

2) Run `python main.py`



