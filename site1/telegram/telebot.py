import time

import telepot

# Токен вашего бота
TOKEN = '5641597027:AAGuUaoQpMPmsxqZwXz1KNwJF6I1P1Pvih0'


# Функция для обработки сообщений
def handle(msg):
    print(telepot.glance(msg))


# Создание объекта бота
bot = telepot.Bot(TOKEN)

# Подписка на события получения сообщений
bot.message_loop(handle)

print('Запустили бота!')

# Запуск бесконечного цикла ожидания событий
while True:
    try:
        time.sleep(10)
    except KeyboardInterrupt:
        break


