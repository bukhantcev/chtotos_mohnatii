from lib2to3.fixes.fix_input import context
from xxlimited_35 import error

from django.shortcuts import render, redirect
from .models import Event, Event_type, Event_name, Event_location
from .forms import EventForm
# Create your views here.


def index(request):



    event_object = Event.objects.order_by('id')
    context = {'event': event_object}

    error = ''
    if 'event_add' in request.POST:
        form = EventForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма не верна'

    form = EventForm(request.POST)
    data = {
        'form': form,
        'error': error
    }

    return render(request, 'forms/index.html', data)

