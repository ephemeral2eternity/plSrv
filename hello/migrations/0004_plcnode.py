# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0003_auto_20141229_1640'),
    ]

    operations = [
        migrations.CreateModel(
            name='PLCNode',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('site_id', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('site', models.CharField(max_length=100)),
                ('node_type', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
