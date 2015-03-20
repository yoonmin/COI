# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_coi', '0032_auto_20150319_1947'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paper',
            old_name='authors',
            new_name='author',
        ),
    ]
