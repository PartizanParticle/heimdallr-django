# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnonPresser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('press_date', models.DateTimeField(verbose_name='Time of button push')),
                ('height', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='KnownPresser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('height', models.FloatField(default=0)),
                ('password', models.CharField(max_length=100)),
                ('last_press', models.DateTimeField(verbose_name='Time of last button push')),
            ],
        ),
    ]
