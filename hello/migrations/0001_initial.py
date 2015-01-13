# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeoSite',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('geom', djgeojson.fields.PointField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PLCNode',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('site_id', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('site', models.CharField(max_length=100)),
                ('node_type', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PLCSite',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('site_name', models.CharField(max_length=200)),
                ('site_url', models.CharField(max_length=1000)),
                ('site_login_base', models.CharField(max_length=100)),
                ('site_longitude', models.DecimalField(max_digits=10, decimal_places=5)),
                ('site_latitude', models.DecimalField(max_digits=10, decimal_places=5)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
