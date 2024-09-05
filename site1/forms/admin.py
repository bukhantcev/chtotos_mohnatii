from django.contrib import admin
from .models import Event, Event_type, Event_name, Event_location

admin.site.register(Event)
admin.site.register(Event_type)
admin.site.register(Event_name)
admin.site.register(Event_location)


# Register your models here.