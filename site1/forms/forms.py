

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
            "type": Select(choices=[('Спектакль', 'Спектакль'), ('Репетиция', 'Репетиция')], attrs={'class': 'form-select mb-1'}),
            "name": Select(choices=[('12', '12'), ('Мет3', 'Мет3')], attrs={'class': 'form-select mb-1'}),
            "location": Select(choices=[('ГИТИС', 'ГИТИС'), ('Сатира', 'Сатира')], attrs={'class': 'form-select mb-1'}),

            "utochneniya": Textarea({'class': 'form-control mb-1', 'placeholder': 'Описание, укзания, примечания и т.д.', 'color': '#ccc'}),






        }

