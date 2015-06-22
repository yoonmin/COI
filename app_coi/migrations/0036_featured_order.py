# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_coi', '0035_auto_20150408_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='featured',
            name='order',
            field=models.IntegerField(default=0, null=True, blank=True),
            preserve_default=True,
        ),
    ]
