# Generated by Django 2.0.9 on 2018-12-14 09:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20181214_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inwardorder',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='outwardorder',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]