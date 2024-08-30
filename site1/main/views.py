from django.shortcuts import render
from .models import calendar, current_year, current_month, calendar_switch_month, my_calendar
from django.http import HttpResponse







def index(request):
    if 'month' in request.GET:
        setattr(my_calendar, 'current_month', int(request.GET.get('month')))

    print(my_calendar.current_month)







    return render(request, 'main/index.html', context={'cal':calendar(result=''), 'current_yer': current_year, 'current_month': my_calendar.month_text[my_calendar.current_month], 'btn_month': calendar_switch_month()})
def about(request):
    return render(request, 'main/about.html')



