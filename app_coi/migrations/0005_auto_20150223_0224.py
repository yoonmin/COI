# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_coi', '0004_faculty_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='email',
            field=models.EmailField(max_length=75, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='faculty',
            name='website',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
    ]
