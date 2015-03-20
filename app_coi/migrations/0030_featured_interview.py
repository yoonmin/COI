# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_coi', '0029_featured_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='featured',
            name='interview',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
