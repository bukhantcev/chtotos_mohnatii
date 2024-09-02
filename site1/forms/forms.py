

from .models import Event
from django.forms import (ModelForm, DateTimeInput, CharField,
                          Textarea, TextInput, MultipleHiddenInput, SelectMultiple,
                          Select, CheckboxInput, CheckboxSelectMultiple)


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['date', 'type', 'name', 'location', 'svet', 'zvuk', 'video', 'decor', 'rekvizit', 'grim', 'kostum', 'utochneniya']
        required = False
        widgets = {
            "date": DateTimeInput({'class': 'form-control mb-1', 'type': 'datetime-local', 'placeholder': 'Дата и время проведения'}),
            "type": Select(choices=[('1', 'First'), ('2', 'Second')], attrs={'class': 'form-select mb-1'}),
            "name": Select(choices=[('1', 'First'), ('2', 'Second')], attrs={'class': 'form-select mb-1'}),
            "location": Select(choices=[('1', 'First'), ('2', 'Second')], attrs={'class': 'form-select mb-1'}),

            "utochneniya": Textarea({'class': 'form-control mb-1', 'placeholder': 'Описание, укзания, примечания и т.д.', 'color': '#ccc'}),






        }

