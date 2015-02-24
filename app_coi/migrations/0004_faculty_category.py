# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_coi', '0003_auto_20150222_2348'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='category',
            field=models.CharField(default=b'D', max_length=3, choices=[(b'D', b'Director'), (b'AD', b'Associate Director'), (b'CFA', b'Columbia Faculty Affiliates'), (b'EFA', b'External Faculty Affiliates')]),
            preserve_default=True,
        ),
    ]
