# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0004_plcnode_node_as'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plcnode',
            name='node_type',
            field=models.CharField(default='unknown', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='plcnode',
            name='site',
            field=models.CharField(default='unknown', max_length=100),
            preserve_default=True,
        ),
    ]
