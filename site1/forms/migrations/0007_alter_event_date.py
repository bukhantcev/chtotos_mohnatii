# Generated by Django 4.2.16 on 2024-09-08 12:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0006_remove_event_type_event_type_name_event_type_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 8, 12, 1, 31, 198875), verbose_name='Дата мероприятия'),
        ),
    ]
