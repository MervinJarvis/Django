# Generated by Django 3.2.3 on 2021-05-21 14:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_pulished',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 21, 20, 1, 27, 60439), verbose_name='Date published'),
        ),
    ]
