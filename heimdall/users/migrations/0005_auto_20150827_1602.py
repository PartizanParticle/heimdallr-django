# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20150827_1559'),
    ]

    operations = [
        migrations.RenameField(
            model_name='press_event',
            old_name='press_date',
            new_name='press_time',
        ),
    ]
