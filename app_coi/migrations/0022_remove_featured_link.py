# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_coi', '0021_auto_20150318_0600'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='featured',
            name='link',
        ),
    ]
