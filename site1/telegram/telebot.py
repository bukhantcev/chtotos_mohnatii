import time

import telepot
from django.template.defaultfilters import first

# Токен вашего бота
TOKEN = '5641597027:AAGuUaoQpMPmsxqZwXz1KNwJF6I1P1Pvih0'


# Функция для обработки сообщений
def handle(msg):
    print(f"{msg['from']['first_name']} {msg['from']['last_name']}")
    print(msg)
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


