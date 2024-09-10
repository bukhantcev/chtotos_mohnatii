from django.shortcuts import render

# Create your views here.
def index(request):#--------------------------------------------ROOM
    print(request.user)
    return render(request, 'room/index.html')