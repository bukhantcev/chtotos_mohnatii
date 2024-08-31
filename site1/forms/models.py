from django.db import models





class Event(models.Model):
    date = models.DateTimeField('Дата мероприятия')
    type = models.CharField('Тип мероприятия', max_length=150)
    name = models.CharField('Название', max_length=150)
    location = models.CharField('Место проведения', max_length=150)
    staff = models.CharField('Службы', max_length=150)


    def __str__(self):
        return f'{self.date} {self.name}'

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'



# events = Event
# for i in events:
#     print(i)