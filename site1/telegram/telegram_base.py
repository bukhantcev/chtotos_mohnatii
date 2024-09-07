# Используем стандартную библиотеку urllib.request
# для того , чтобы делать запросы.
# Можно использовать сторонние библиотеки requests или httpx
import urllib.request
import json
from forms.models import Event
from django.shortcuts import get_object_or_404


# Тут будет ваш токен, который вы получили при создании бота
BOT_TOKEN = "5641597027:AAGuUaoQpMPmsxqZwXz1KNwJF6I1P1Pvih0"

# Тут нужно указать название канала в ссылке,которое начинается с @
# Тут я указал для примера созданный канал
CHAT_ID = "-1002403221230"


def send_telegram_message(id):
    event = get_object_or_404(Event,id=id)
    ev_data = f'{str(event.date).split(' ')[0].split("-")[2]}.{str(event.date).split(' ')[0].split("-")[1]}.{str(event.date).split(' ')[0].split("-")[0]}'
    ev_time = f'{str(event.date).split(' ')[1].split(':')[0]}:{str(event.date).split(' ')[1].split(':')[1]}'
    ev_staff = f'Свет - {'Да' if event.svet == 'on' else 'Нет'}\nЗвук - {'Да' if event.zvuk == 'on' else 'Нет'}\nВидео - {'Да' if event.video == 'on' else 'Нет'}\nДекорации - {'Да' if event.decor == 'on' else 'Нет'}\nРеквизит - {'Да' if event.rekvizit == 'on' else 'Нет'}\nГрим - {'Да' if event.grim == 'on' else 'Нет'}\nКостюм - {'Да' if event.kostum == 'on' else 'Нет'}'
    text = text_message = f'Дата: {ev_data}\n\nВремя: {ev_time}\n\nМесто проведения: {event.location}\n\n{event.type} "{event.name}"\n\nВызываются службы: \n{ev_staff}\n\nОписание: {event.utochneniya}'
    # Используется метод sendMessage API Telegram
    # Обратите внимание , что мы тут используем BOT_TOKEN
    api_url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'

    #Указаваем в параметрах CHAT_ID и само сообщение
    input_data = json.dumps(
        {
            'chat_id': CHAT_ID,
            'text': text,
        }
    ).encode()

    try:
        req = urllib.request.Request(
            url=api_url,
            data=input_data,
            headers={'Content-Type': 'application/json'}
        )
        with urllib.request.urlopen(req) as response:
            #Тут выводим ответ
            print(response.read().decode('utf-8'))

    except Exception as e:
        print(e)





# if __name__ == "__main__":
#     send_telegram_message()

# 404354012