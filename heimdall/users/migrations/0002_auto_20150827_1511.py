# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='anonpresser',
            name='imgName',
            field=models.CharField(max_length=50, default='fail.jpg'),
        ),
        migrations.AddField(
            model_name='knownpresser',
            name='imgName',
            field=models.CharField(max_length=50, default='fail.jpg'),
        ),
    ]
