# Generated by Django 3.1.5 on 2021-02-07 18:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 7, 18, 13, 44, 237335), verbose_name='date published'),
        ),
    ]
