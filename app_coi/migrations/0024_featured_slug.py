# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_coi', '0023_auto_20150318_2211'),
    ]

    operations = [
        migrations.AddField(
            model_name='featured',
            name='slug',
            field=models.SlugField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
    ]
