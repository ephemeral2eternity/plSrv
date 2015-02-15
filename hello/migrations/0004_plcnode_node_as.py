# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0003_plcnode_node_ip'),
    ]

    operations = [
        migrations.AddField(
            model_name='plcnode',
            name='node_as',
            field=models.CharField(max_length=500, default='unknown'),
            preserve_default=True,
        ),
    ]
