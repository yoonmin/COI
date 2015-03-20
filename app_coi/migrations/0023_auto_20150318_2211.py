# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_coi', '0022_remove_featured_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='featured',
            old_name='img',
            new_name='thumb',
        ),
        migrations.AddField(
            model_name='featured',
            name='name',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
    ]
