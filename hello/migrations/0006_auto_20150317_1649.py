# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0005_auto_20150226_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='plcnode',
            name='region',
            field=models.CharField(max_length=100, default='unknown'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='plcnode',
            name='zone',
            field=models.CharField(max_length=100, default='unknown'),
            preserve_default=True,
        ),
    ]
