# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_coi', '0024_featured_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='featured',
            old_name='description',
            new_name='summary',
        ),
    ]
