from django.db import models
from django.template.context_processors import request







class Event(models.Model):
    date = models.DateTimeField('Дата мероприятия')
    type = models.CharField('Тип мероприятия', max_length=150)
    name = models.CharField('Название', max_length=150)
    location = models.CharField('Место проведения', max_length=150)
    svet = models.CharField('Свет', max_length=150)
    zvuk = models.CharField('Звук', max_length=150)
    video = models.CharField('Видео', max_length=150)
    decor = models.CharField('Декорация', max_length=150)
    rekvizit = models.CharField('Реквизит', max_length=150)
    grim = models.CharField('Грим', max_length=150)
    kostum = models.CharField('Костюм', max_length=150)
    utochneniya = models.TextField('Уточнения', default='')


    def __str__(self):
        return f'{self.date} {self.name}'

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'



# events = Event
# for i in events:
#     print(i)