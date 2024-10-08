# Generated by Django 5.1 on 2024-09-02 13:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0002_alter_event_options_event_utochneniya'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='staff',
        ),
        migrations.AddField(
            model_name='event',
            name='decor',
            field=models.CharField(default='', max_length=150, verbose_name='Декорация'),
        ),
        migrations.AddField(
            model_name='event',
            name='grim',
            field=models.CharField(default='', max_length=150, verbose_name='Грим'),
        ),
        migrations.AddField(
            model_name='event',
            name='kostum',
            field=models.CharField(default='', max_length=150, verbose_name='Костюм'),
        ),
        migrations.AddField(
            model_name='event',
            name='rekvizit',
            field=models.CharField(default='', max_length=150, verbose_name='Реквизит'),
        ),
        migrations.AddField(
            model_name='event',
            name='svet',
            field=models.CharField(default='', max_length=150, verbose_name='Свет'),
        ),
        migrations.AddField(
            model_name='event',
            name='video',
            field=models.CharField(default='', max_length=150, verbose_name='Видео'),
        ),
        migrations.AddField(
            model_name='event',
            name='zvuk',
            field=models.CharField(default='', max_length=150, verbose_name='Звук'),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 2, 16, 30, 18, 358514), verbose_name='Дата мероприятия'),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(default='', max_length=150, verbose_name='Место проведения'),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(default=' ', max_length=150, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='event',
            name='type',
            field=models.CharField(default='', max_length=150, verbose_name='Тип мероприятия'),
        ),
    ]
