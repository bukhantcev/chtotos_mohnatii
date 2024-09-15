import datetime

from dateutil.utils import today
from django.shortcuts import render, redirect
from .models import calendar, calendar_switch_month, my_calendar, calendar_switch_year, autoscroll

from telegram.telegram_base import send_telegram_message







def index(request):       #-------------MAIN
    author = f"{request.user.first_name} {request.user.last_name}"
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






