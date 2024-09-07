# Generated by Django 4.2.16 on 2024-09-05 06:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0003_remove_event_staff_event_decor_event_grim_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event_location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(default='', max_length=150, verbose_name='Место проведения')),
                ('city', models.CharField(blank=True, default='', max_length=150, verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Место проведения события',
                'verbose_name_plural': 'Места проведения событий',
            },
        ),
        migrations.CreateModel(
            name='Event_name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=150, verbose_name='Место проведения')),
            ],
            options={
                'verbose_name': 'Название события',
                'verbose_name_plural': 'Названия событий',
            },
        ),
        migrations.CreateModel(
            name='Event_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default='', max_length=150, verbose_name='Тип события')),
            ],
            options={
                'verbose_name': 'Тип события',
                'verbose_name_plural': 'Типы событий',
            },
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 5, 9, 31, 33, 72230), verbose_name='Дата мероприятия'),
        ),
        migrations.AlterField(
            model_name='event',
            name='decor',
            field=models.CharField(blank=True, default='', max_length=150, verbose_name='Декорация'),
        ),
        migrations.AlterField(
            model_name='event',
            name='grim',
            field=models.CharField(blank=True, default='', max_length=150, verbose_name='Грим'),
        ),
        migrations.AlterField(
            model_name='event',
            name='kostum',
            field=models.CharField(blank=True, default='', max_length=150, verbose_name='Костюм'),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(blank=True, default='', max_length=150, verbose_name='Место проведения'),
        ),
        migrations.AlterField(
            model_name='event',
            name='rekvizit',
            field=models.CharField(blank=True, default='', max_length=150, verbose_name='Реквизит'),
        ),
        migrations.AlterField(
            model_name='event',
            name='svet',
            field=models.CharField(blank=True, default='', max_length=150, verbose_name='Свет'),
        ),
        migrations.AlterField(
            model_name='event',
            name='utochneniya',
            field=models.TextField(blank=True, default='', verbose_name='Уточнения'),
        ),
        migrations.AlterField(
            model_name='event',
            name='video',
            field=models.CharField(blank=True, default='', max_length=150, verbose_name='Видео'),
        ),
        migrations.AlterField(
            model_name='event',
            name='zvuk',
            field=models.CharField(blank=True, default='', max_length=150, verbose_name='Звук'),
        ),
    ]
