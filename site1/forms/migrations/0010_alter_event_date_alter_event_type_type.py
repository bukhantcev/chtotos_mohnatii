# Generated by Django 4.2.16 on 2024-09-08 13:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0009_alter_event_date_alter_event_type_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 8, 13, 24, 4, 779704), verbose_name='Дата мероприятия'),
        ),
        migrations.AlterField(
            model_name='event_type',
            name='type',
            field=models.CharField(max_length=150, verbose_name='Тип мероприятия'),
        ),
    ]
