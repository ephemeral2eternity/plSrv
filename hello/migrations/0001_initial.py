# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-12 16:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PLCNode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_id', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('site', models.CharField(default='unknown', max_length=100)),
                ('zone', models.CharField(default='unknown', max_length=100)),
                ('region', models.CharField(default='unknown', max_length=100)),
                ('node_type', models.CharField(default='unknown', max_length=200)),
                ('node_ip', models.CharField(default='0.0.0.0', max_length=20)),
                ('node_os', models.CharField(default='unknown', max_length=200)),
                ('node_as', models.CharField(default='unknown', max_length=500)),
                ('node_python', models.CharField(default='unknown', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PLCSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=200)),
                ('site_url', models.CharField(max_length=1000)),
                ('site_login_base', models.CharField(max_length=100)),
                ('site_longitude', models.DecimalField(decimal_places=5, max_digits=10)),
                ('site_latitude', models.DecimalField(decimal_places=5, max_digits=10)),
            ],
        ),
    ]
