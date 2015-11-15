# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='weather',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('weather_time', models.DateTimeField(verbose_name='Timestamp of weather info')),
                ('temperature', models.FloatField(default=0)),
                ('humidity', models.FloatField(default=0)),
            ],
        ),
    ]
