# Generated by Django 2.0.9 on 2018-12-05 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('firm', models.CharField(max_length=80)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=50)),
                ('mobile_number', models.IntegerField()),
            ],
        ),
    ]
