# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plcnode',
            name='node_os',
            field=models.CharField(max_length=200, default='unknown'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='plcnode',
            name='node_python',
            field=models.CharField(max_length=200, default='unknown'),
            preserve_default=True,
        ),
    ]
