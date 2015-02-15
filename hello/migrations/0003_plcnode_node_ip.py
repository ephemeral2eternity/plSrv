# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_auto_20150109_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='plcnode',
            name='node_ip',
            field=models.CharField(default='0.0.0.0', max_length=20),
            preserve_default=True,
        ),
    ]
