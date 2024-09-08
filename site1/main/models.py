import datetime
from calendar import monthrange
from .db_manager import Events
from forms.models import Event
from django.contrib.auth.models import User

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


def calendar (result='', user_valid=False):       #--------------------------------------------DAYS
    current_year = my_calendar.current_year
    current_month = my_calendar.current_month
    days_quantity = monthrange(current_year, current_month)[1]
    weekdays = {0: 'Понедельник', 1: 'Вторник', 2: 'Среда', 3: 'Четверг', 4: 'Пятница', 5: 'Суббота', 6: 'Воскресенье'}
    events = Events.events(Events)
    event_dates = Events.get_date(Events)


    button_tg1 = '<a href="?text_message=' if user_valid == True else ''
    button_tg2 = '" type="submit">Отравить в телегу</a>' if user_valid == True else ''


    for i in range(days_quantity):
        event_li = ''
        date = datetime.datetime(current_year, current_month, i+1)
        event_object = Event.objects.order_by('date')

        for event in event_object:
            id = f'event_id{event.id}'
            ev_name = event.name
            ev_date = event.date
            ev_time =   f'{str(ev_date).split(' ')[1].split(':')[0]}:{str(ev_date).split(' ')[1].split(':')[1]}'

            ev_type = event.type
            ev_location = event.location
            ev_utochneniya = f'<h5 style="color: red">Описание:<br></h5><p>{event.utochneniya}</p>' if event.utochneniya!='' else ''
            ev_staff = f'Свет - {event.svet}<br>Звук - {event.zvuk}<br>Видео - {event.video}<br>Декорации - {event.decor}<br>Реквизит - {event.rekvizit}<br>Грим - {event.grim}<br>Костюм - {event.kostum}'
            if str(date).split(' ')[0] in str(ev_date).split(' ')[0]:
                event_li = event_li + f'''<button type="button" class="btn btn-primary" style="font-size: 0.8rem; margin-bottom: 0.1rem; width: 100%" data-bs-toggle="modal" data-bs-target="#{id}">
  {ev_time} &quot;{ev_name}&quot; ({ev_type})
</button>

<!-- Modal -->
<div class="modal fade" style="width: 100%" id="{id}" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h3 class="modal-title" id="exampleModalLabel">{ev_type} &quot;{ev_name}&quot;&nbsp;&nbsp;Время: {ev_time}</h3>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
      <div class="modal-body">
        <h5 style="color: red">Место проведения: <p style="color: #000"><br>{ev_location}</p><br></h5>

        {ev_utochneniya}
        <h5 style="color: red">Вызываются службы:<br></h5>
        <p>{ev_staff}</p>
        
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        {button_tg1}{event.id if user_valid == True else ''}{button_tg2}
      </div>
    </div>
  </div>
</div>\n'''
        result = result + f'<div class="col h-100"><div class="card" style="height: 20rem" ><div class="card-header" style="font-size: 1rem">{i+1} {weekdays[date.weekday()]}</div><div class="card-body"><ul style="margin-right: 2rem">{event_li}</ul></p></div></div></div>\n'
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
