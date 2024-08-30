from django.shortcuts import render
from .models import calendar, current_year, current_month, calendar_switch_month
from django.http import HttpResponse







def index(request):
    print(request.POST.get)

    print(request.GET.get('month'))







    return render(request, 'main/index.html', context={'cal':calendar(result=''), 'current_yer': current_year, 'current_month': current_month, 'btn_month': calendar_switch_month()})
def about(request):
    return render(request, 'main/about.html')
