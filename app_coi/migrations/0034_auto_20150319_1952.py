# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_coi', '0033_auto_20150319_1952'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paper',
            old_name='link',
            new_name='pdf',
        ),
    ]
