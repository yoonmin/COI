# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_coi', '0031_paper'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='link',
            field=models.FileField(null=True, upload_to=b'papers', blank=True),
            preserve_default=True,
        ),
    ]
