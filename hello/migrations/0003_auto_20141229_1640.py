# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_geosite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geosite',
            name='geom',
            field=djgeojson.fields.PointField(),
            preserve_default=True,
        ),
    ]
