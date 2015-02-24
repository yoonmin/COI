# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_coi', '0002_auto_20150222_2347'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='People_Faculty',
            new_name='Faculty',
        ),
    ]
