# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_coi', '0020_auto_20150317_2128'),
    ]

    operations = [
        migrations.CreateModel(
            name='Featured',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('link', models.URLField(blank=True)),
                ('cover', models.ImageField(upload_to=b'featured', blank=True)),
                ('img', models.ImageField(upload_to=b'featured', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='visitingscholar',
            name='category',
            field=models.CharField(default=b'C', max_length=1, choices=[(b'C', b'Current Visiting Scholar'), (b'P', b'Past Visiting Scholar')]),
            preserve_default=True,
        ),
    ]
