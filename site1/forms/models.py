from django.db import models
from django.template.context_processors import request
from datetime import datetime







class Event(models.Model):
    date = models.DateTimeField('Дата мероприятия', default=datetime.now())
    type = models.CharField('Тип мероприятия', max_length=150, default='')
    name = models.CharField('Название', max_length=150, default=' ')
    location = models.CharField('Место проведения', max_length=150, default='', blank=True)
    svet = models.CharField('Свет', max_length=150, default='', blank=True)
    zvuk = models.CharField('Звук', max_length=150, default='', blank=True)
    video = models.CharField('Видео', max_length=150, default='', blank=True)
    decor = models.CharField('Декорация', max_length=150, default='', blank=True)
    rekvizit = models.CharField('Реквизит', max_length=150, default='', blank=True)
    grim = models.CharField('Грим', max_length=150, default='', blank=True)
    kostum = models.CharField('Костюм', max_length=150, default='', blank=True)
    utochneniya = models.TextField('Уточнения', default='', blank=True)


    def __str__(self):
        return f'{self.date} {self.name}'

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'



# events = Event
# for i in events:
#     print(i)