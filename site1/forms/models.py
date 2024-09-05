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



class Event_type(models.Model):

    type = models.CharField('Тип события', max_length=150, default='')



    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Тип события'
        verbose_name_plural = 'Типы событий'


class Event_location(models.Model):
    location = models.CharField('Место проведения', max_length=150, default='')
    city = models.CharField('Город', max_length=150, default='', blank=True)


    def __str__(self):
        return f'{self.location} {self.city}'

    class Meta:
        verbose_name = 'Место проведения события'
        verbose_name_plural = 'Места проведения событий'


class Event_name(models.Model):
    name = models.CharField('Место проведения', max_length=150, default='')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Название события'
        verbose_name_plural = 'Названия событий'







# events = Event
# for i in events:
#     print(i)