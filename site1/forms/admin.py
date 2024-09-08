from django.contrib import admin
from .models import Event, Event_type, Event_name, Event_location

# admin.site.register(Event)
admin.site.register(Event_type)
admin.site.register(Event_name)
admin.site.register(Event_location)



@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('date', 'name', 'type', 'location' ,)
    liink_display = ('date')
    list_editable = ('type',)


# Register your models here.