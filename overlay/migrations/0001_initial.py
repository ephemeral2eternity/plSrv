# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Edge',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('src', models.CharField(max_length=10)),
                ('dst', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('ip', models.CharField(max_length=20)),
                ('zone', models.CharField(max_length=20, default='')),
                ('type', models.CharField(max_length=50, default='f1-micro')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
