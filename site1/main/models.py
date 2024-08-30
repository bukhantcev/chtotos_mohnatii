from typing import final

from django.db import models
import datetime
from calendar import monthrange

# Create your models here.

# Calendar

month_text = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь', 7: 'Июль', 8: 'Август',
                  9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}
current_year = datetime.datetime.now().year
current_month = month_text[datetime.datetime.now().month]





def calendar (result=''):
    current_year = datetime.datetime.now().year
    current_month = datetime.datetime.now().month
    days_quantity = monthrange(current_year, current_month)[1]
    weekdays = {0: 'Понедельник', 1: 'Вторник', 2: 'Среда', 3: 'Четверг', 4: 'Пятница', 5: 'Суббота', 6: 'Воскресенье'}


    for i in range(days_quantity):
        date = datetime.datetime(current_year, current_month, i+1)
        result = result + f'<div class=col><div class=card><div class=card-header>{i+1} {weekdays[date.weekday()]}</div><div class=card-body><a class=link-sobitie href="#"><p class=sobitie>Kakoe-to sobitie</a></p><div class=card-footer>footer</div></div></div></div>\n'
    return result

def calendar_switch_month():
    month_text = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь', 7: 'Июль', 8: 'Август',
                  9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}
    current_month = datetime.datetime.now().month
    result = []
    final = ''
    for i in range(11):
        ind = current_month
        if i < (12-ind):
            ind2 = 0
            ind = ind+i +1
            result.append(ind)
        else:
            ind2 = ind2 + 1
            result.append(ind2)
    for i in result:
        final = final + f'<li><a class="dropdown-item" href="?month={i}" type="submit">{month_text[i]}</a></li>' + '\n'




    return final

