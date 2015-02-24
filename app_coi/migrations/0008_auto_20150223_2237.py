# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_coi', '0007_alumni_currentstudent_visitingscholar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='category',
            field=models.CharField(default=b'D', max_length=3, choices=[(b'D', b'Director'), (b'AD', b'Associate Director'), (b'CFA', b'Columbia Faculty Affiliate'), (b'EFA', b'External Faculty Affiliate')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='visitingscholar',
            name='category',
            field=models.CharField(default=b'C', max_length=1, choices=[(b'C', b'Current Scholar'), (b'P', b'Past Scholar')]),
            preserve_default=True,
        ),
    ]
