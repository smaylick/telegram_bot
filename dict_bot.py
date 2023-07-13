# В google colab добавить: !pip install pyTelegramBotAPI
# Чтобы добавить новое слово — нужно его прописать в объект DEFINITOINS на 13 строчке
# Важно все новые аббривиатуры в коде писать только с маленьких букв
# Пользователь в телеграм может писать и с большой и с маленькой — код всегда приводит к строчным

from telebot import TeleBot, types

bot = TeleBot(token='введите_токен', parse_mode='html') # создание бота

# словарь с определениями и аббревиатурами, которые знает бот
# в формате:
# 'ключевая фраза': 'соответствующее ей определение'
DEFINITOINS = {
    'регресс': 'проверить что новый функционал не сломал существующий',
    'тестирование': 'процесс анализа программного средства и сопутствующей документации с целью выявления дефектов и повышения качества продукта',
    'клиент': 'любая программа, через которую пользователь инициирует запрос на сервер',
    'сервер': 'мощный компьютер, на котором храниться приложение с его логикой и базой данных',
    'api': 'разновидность интерфейсов, предназначенная для взаимодействия программ между собой. Т.е. это способы взаимодействия программ друг с другом.',
    'postman': 'программа-клиент с помощью которой можно тестировать бекенд',
    'agile': 'итеративный способ/подход, основанный на ценностях и принципах гибким управлением проектами и разработки ПО',
    'scrum': 'это фреймворк/методология, который/ая определяет инструменты и процессы для обеспечения гибкого процесса разработки',
}

# обработчик команды '/start'
@bot.message_handler(commands=['start'])
def start_command_handler(message: types.Message):
    # отправляем ответ на команду '/start'
    bot.send_message(
        chat_id=message.chat.id, # id чата, в который необходимо направить сообщение
        text='Привет! Я помогу тебе дать определения терминам из лекций!😎\nВот список доступных слов:\n- тестирование\n- клиент\n- сервер\n- api\n- postman\n- agile\n- scrum\n- регресс\n \nВведи любой термин из доступных, например тестирование', # текст сообщения
    )

# обработчик всех остальных сообщений
@bot.message_handler()
def message_handler(message: types.Message):
    # пробуем найти ключевую фразу в словаре
    definition = DEFINITOINS.get(
        message.text.lower(), # приводим текст сообщения к нижнему регистру
    )
    # если фразы нет в словаре, то переменная definition будет иметь значение None
    # проверяем это условие
    if definition is None:
        # если ключевая фраза не была найдена в словаре
        # отправляем ответ
        bot.send_message(
            chat_id=message.chat.id,
            text='😋 Я пока не знаю такого определения',
        )
        # выходим из функции
        return
    
    # если ключевая фраза была найдена, формируем текст сообщения и отправляем его
    # если перед строкой поставить букву f, то в фигурных скобках {} можно использовать переменные :)
    bot.send_message(
        chat_id=message.chat.id,
        text=f'Держи определение:\n<code>{definition}</code>',
    )

    bot.send_message(
        chat_id=message.chat.id,
        text=f'Жду следующий термин',
    )


# главная функция программы
def main():
    # запускаем нашего бота
    bot.infinity_polling()


if __name__ == '__main__':
    main()
