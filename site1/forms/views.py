from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from .models import Event
# Create your views here.


def index(request):
    events = Event.objects.all()

    return render(request, 'forms/index.html', {'events':events})

