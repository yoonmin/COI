# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_coi', '0010_auto_20150317_1918'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Alumni',
        ),
        migrations.DeleteModel(
            name='CurrentStudent',
        ),
    ]
