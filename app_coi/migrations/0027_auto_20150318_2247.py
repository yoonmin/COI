# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_coi', '0026_auto_20150318_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featured',
            name='cv',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
