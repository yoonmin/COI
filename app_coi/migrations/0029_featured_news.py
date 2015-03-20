# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_coi', '0028_featured_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='featured',
            name='news',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
