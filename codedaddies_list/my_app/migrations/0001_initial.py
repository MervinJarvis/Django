# Generated by Django 3.2.3 on 2021-06-09 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search', models.CharField(max_length=2000)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Searches',
            },
        ),
    ]
