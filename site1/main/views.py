import datetime

from dateutil.utils import today
from django.shortcuts import render, redirect
from .models import calendar, calendar_switch_month, my_calendar, calendar_switch_year, autoscroll
from forms.models import Event_name, Event, Event_type, Event_location

from telegram.telegram_base import send_telegram_message
from forms.parser import create_event

from django.forms.models import model_to_dict








def index(request):       #-------------MAIN
    if "command" in request.GET:    #-----ПАРСИНГ С САЙТА
        if 'go_parsing' in request.GET.get('command'):
            event_names = Event_name.objects.all()

            for name in create_event():
                event_names = Event_name.objects.all()
                index = 0
                for event in event_names:

                    if name['name'] == str(event):
                        index = 1
                if index == 0:
                    record = Event_name(name=name['name'])
                    record.save()

            for new_event in create_event():
                record = Event(date=new_event['date'], name=Event_name.objects.get(name=new_event['name']), type=Event_type.objects.get(type="Спектакль"), location=Event_location.objects.get(location='ГИТИС'))
                record.save()
        return redirect('/')
                #--------ПАРСИНГ С САЙТА







    try:
        author = f"{request.user.first_name} {request.user.last_name}"
    except:
        author = request.user.username
    if 'text_message' in request.GET:
        if request.user.is_staff:
            send_telegram_message(request.GET.get('text_message'), author=author)
            return(redirect('/'))
    if 'month' in request.GET:
        setattr(my_calendar, 'current_month', int(request.GET.get('month')))
    if 'year' in request.GET:

        if request.GET.get('year') == 'current':
            setattr(my_calendar, 'current_year', calendar_switch_year()['current_year'])
        if request.GET.get('year') == 'next':
            setattr(my_calendar, 'current_year', calendar_switch_year()['next_year'])
        if request.GET.get('year') == 'real':
            setattr(my_calendar, 'current_year', calendar_switch_year()['real_year'])
        setattr(my_calendar, 'year_title', my_calendar.current_year)
    if 'home' in request.GET:
        setattr(my_calendar, 'current_year', datetime.datetime.now().year)
        setattr(my_calendar, 'year_title', datetime.datetime.now().year)
        setattr(my_calendar, 'current_month', datetime.datetime.now().month)
    if request.user.is_authenticated:#-------TODAY
        today = f'#id_card_{datetime.datetime.now().day}'
        card_bg_color = 'background-color: #07bc25'
        if 'month' in request.GET:
            if int(request.GET.get('month')) == datetime.datetime.now().month:
                today = autoscroll()
                card_bg_color = 'background-color: #07bc25'
            else:
                today = '#main'
                card_bg_color = ''#------TODAY


        return render(request, 'main/index.html', context={'cal':calendar(result='', user_valid=request.user.is_staff,card_header_bg_color=card_bg_color, author=author), 'current_month': my_calendar.month_text[my_calendar.current_month], 'btn_month': calendar_switch_month(), 'current_year': calendar_switch_year()['current_year'], 'next_year': calendar_switch_year()['next_year'], 'real_year': calendar_switch_year()['real_year'], 'today': today, 'year_title': my_calendar.year_title})
    else:
        return redirect('login')



def about(request):#--------------------------------------------ABOUT
    return render(request, 'main/about.html')






