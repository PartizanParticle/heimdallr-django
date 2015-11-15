# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20150827_1558'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AnonPresser',
            new_name='press_event',
        ),
    ]
