

from .models import Event, Event_type, Event_name, Event_location
from django.forms import (ModelForm, DateTimeInput, CharField,
                          Textarea, TextInput, MultipleHiddenInput, SelectMultiple,
                          Select, CheckboxInput, CheckboxSelectMultiple)


class EventForm(ModelForm):
    class Meta:
        event_type = Event_type.objects.order_by('id')
        event_name = Event_name.objects.order_by('id')
        event_location = Event_location.objects.order_by('id')
        event_type_list = []
        event_name_list = []
        event_location_list = []
        try:

            for i in event_type:
                event_type_list.append((i.type,i.type))
        except:
            event_type_list.append(("Нет вариантов", "Нет вариантов"))
        try:
            for i in event_name:
                event_name_list.append((i.name,i.name))
        except:
            event_name_list.append(("Нет вариантов", "Нет вариантов"))
        try:
            for i in event_location:
                event_location_list.append((i.location,i.location))

        except:
            event_location_list.append(("Нет вариантов", "Нет вариантов"))



        model = Event
        fields = ['date', 'type', 'name', 'location', 'svet', 'zvuk', 'video', 'decor', 'rekvizit', 'grim', 'kostum', 'utochneniya']
        required = False
        widgets = {
            "date": DateTimeInput({'class': 'form-control mb-1', 'type': 'datetime-local', 'placeholder': 'Дата и время проведения'}),
            "type": Select(choices=event_type_list, attrs={'class': 'form-select mb-1', 'placeholder': 'Выбери тип события'}),
            "name": Select(choices=event_name_list, attrs={'class': 'form-select mb-1'}),
            "location": Select(choices=event_location_list, attrs={'class': 'form-select mb-1'}),

            "utochneniya": Textarea({'class': 'form-control mb-1', 'placeholder': 'Описание, укзания, примечания и т.д.', 'color': '#ccc'}),






        }

