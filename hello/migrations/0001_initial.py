# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PLCSite',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('site_name', models.CharField(max_length=200)),
                ('site_url', models.CharField(max_length=1000)),
                ('site_login_base', models.CharField(max_length=100)),
                ('site_longitude', models.DecimalField(decimal_places=5, max_digits=10)),
                ('site_latitude', models.DecimalField(decimal_places=5, max_digits=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
