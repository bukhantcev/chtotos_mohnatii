import datetime
from datetime import tzinfo, timezone, timedelta

from django.shortcuts import render, redirect
from .models import calendar, current_year, current_month, calendar_switch_month, my_calendar, calendar_switch_year
from django.http import HttpResponse
from forms.models import Event
from telegram.telegram_base import send_telegram_message
from django.contrib.auth.models import User






def index(request):       #-------------MAIN
    if 'text_message' in request.GET:
        if User.is_staff:
            send_telegram_message(request.GET.get('text_message'))
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
    if request.user.is_authenticated:
        return render(request, 'main/index.html', context={'cal':calendar(result=''), 'current_month': my_calendar.month_text[my_calendar.current_month], 'btn_month': calendar_switch_month(), 'current_year': calendar_switch_year()['current_year'], 'next_year': calendar_switch_year()['next_year'], 'real_year': calendar_switch_year()['real_year'], 'year_title': my_calendar.year_title})
    else:
        return redirect('login')



def about(request):#--------------------------------------------ABOUT
    return render(request, 'main/about.html')






