# Generated by Django 5.1 on 2024-08-31 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name': 'Клиент', 'verbose_name_plural': 'Клиенты'},
        ),
    ]
