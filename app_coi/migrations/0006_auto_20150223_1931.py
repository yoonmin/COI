# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app_coi', '0005_auto_20150223_0224'),
    ]

    operations = [
        migrations.RenameField(
            model_name='faculty',
            old_name='name',
            new_name='firstname',
        ),
        migrations.AddField(
            model_name='faculty',
            name='lastname',
            field=models.CharField(default=datetime.datetime(2015, 2, 23, 19, 31, 22, 865417, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
