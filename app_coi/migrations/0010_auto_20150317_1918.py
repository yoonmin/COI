# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_coi', '0009_auto_20150224_0248'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to=b'media/people')),
                ('description', models.TextField()),
                ('email', models.EmailField(max_length=75, blank=True)),
                ('website', models.URLField(blank=True)),
                ('category', models.CharField(default=b'C', max_length=1, choices=[(b'C', b'Current Students'), (b'A', b'Alumni')])),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='category',
            field=models.CharField(default=b'D', max_length=1, choices=[(b'D', b'Director'), (b'A', b'Associate Director'), (b'C', b'Columbia Faculty Affiliate'), (b'E', b'External Faculty Affiliate')]),
            preserve_default=True,
        ),
    ]
