# Generated by Django 5.1 on 2024-09-01 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'Событие', 'verbose_name_plural': 'События'},
        ),
        migrations.AddField(
            model_name='event',
            name='utochneniya',
            field=models.TextField(default='', verbose_name='Уточнения'),
        ),
    ]
