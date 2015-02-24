# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_coi', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Faculty',
            new_name='People_Faculty',
        ),
    ]
