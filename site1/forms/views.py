from django.shortcuts import render

# Create your views here.


def index(request):       #-------------MAIN

    return render(request, 'forms/index.html')

