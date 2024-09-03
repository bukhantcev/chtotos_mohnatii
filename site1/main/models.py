import datetime
from calendar import monthrange
from .db_manager import Events

# Create your models here.

# Calendar
                 #----------------------------------------CALENDAR
month_text = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь', 7: 'Июль', 8: 'Август',
                  9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}
current_year = datetime.datetime.now().year
current_month = month_text[datetime.datetime.now().month]


class Calendar:
    current_year = datetime.datetime.now().year
    current_month = datetime.datetime.now().month
    year_title = current_year

    month_text = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь', 7: 'Июль', 8: 'Август',
                  9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}

    def cal_text(current_month):
        return month_text(current_month)

my_calendar = Calendar


def calendar (result=''):       #--------------------------------------------DAYS
    current_year = my_calendar.current_year
    current_month = my_calendar.current_month
    days_quantity = monthrange(current_year, current_month)[1]
    weekdays = {0: 'Понедельник', 1: 'Вторник', 2: 'Среда', 3: 'Четверг', 4: 'Пятница', 5: 'Суббота', 6: 'Воскресенье'}
    events = Events.events(Events)
    event_dates = Events.get_date(Events)


    for i in range(days_quantity):
        event_li = ''
        date = datetime.datetime(current_year, current_month, i+1)
        for event in events:
            id = event[0]
            ev_name = event[3]
            ev_time = f'{str(event[1]).split(' ')[1].split(':')[0]}:{str(event[1]).split(' ')[1].split(':')[1]}'
            ev_date = event[1]
            ev_type = event[2]
            if str(date).split(' ')[0] in str(ev_date).split(' ')[0]:
                event_li = event_li + f'<li class="event_li"><button class="btn btn-succes" id="event_id_{id}" name="event_id" onclick="Ajax()" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasCardEvent" aria-controls="#offcanvasCardEvent">{ev_time} {ev_name}({ev_type})</button></li>\n'
        result = result + f'<div class="col h-100"><div class="card" style="height: 15rem"><div class="card-header">{i+1} {weekdays[date.weekday()]}</div><div class="card-body"><ul>{event_li}</ul></p></div></div></div>\n'
    return result

def calendar_switch_month(): #---------------------MONTS
    month_text = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь', 7: 'Июль', 8: 'Август',
                  9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}
    result = []
    final = ''
    ind2 = 0
    for i in range(11):
        ind = my_calendar.current_month
        if i < (12-ind):

            ind = ind+i +1
            result.append(ind)
        else:
            ind2 = ind2 + 1
            result.append(ind2)
    for i in result:
        final = final + f'<li><a class="dropdown-item" href="?month={i}" type="submit">{month_text[i]}</a></li>' + '\n'




    return final


def calendar_switch_year(): #__________________________________YEARS
    current_year = my_calendar.current_year
    next_year = my_calendar.current_year + 1
    real_year = datetime.datetime.now().year
    return {'current_year': current_year, 'next_year': next_year, 'real_year': real_year}
#----------------------------------------------------------------------------------------CALENDAR
