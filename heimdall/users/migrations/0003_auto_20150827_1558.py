# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20150827_1511'),
    ]

    operations = [
        migrations.DeleteModel(
            name='KnownPresser',
        ),
        migrations.RenameField(
            model_name='anonpresser',
            old_name='imgName',
            new_name='img_name',
        ),
        migrations.AddField(
            model_name='anonpresser',
            name='known_person',
            field=models.BooleanField(default=False),
        ),
    ]
