# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import app_coi.models


class Migration(migrations.Migration):

    dependencies = [
        ('app_coi', '0034_auto_20150319_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='img',
            field=models.ImageField(storage=app_coi.models.OverwriteStorage(), upload_to=b'people'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='featured',
            name='cover',
            field=models.ImageField(storage=app_coi.models.OverwriteStorage(), upload_to=b'featured', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='featured',
            name='thumb',
            field=models.ImageField(storage=app_coi.models.OverwriteStorage(), upload_to=b'featured', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='paper',
            name='pdf',
            field=models.FileField(storage=app_coi.models.OverwriteStorage(), null=True, upload_to=b'papers', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='img',
            field=models.ImageField(storage=app_coi.models.OverwriteStorage(), upload_to=b'people'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='visitingscholar',
            name='img',
            field=models.ImageField(storage=app_coi.models.OverwriteStorage(), upload_to=b'people'),
            preserve_default=True,
        ),
    ]
