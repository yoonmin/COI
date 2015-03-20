# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_coi', '0019_auto_20150317_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitingscholar',
            name='category',
            field=models.CharField(default=b'P', max_length=1, choices=[(b'C', b'Current Visiting Scholar'), (b'P', b'Past Visiting Scholar')]),
            preserve_default=True,
        ),
    ]
