# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RTTs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('az01', models.DecimalField(max_digits=10, decimal_places=5, default=10000.0)),
                ('az02', models.DecimalField(max_digits=10, decimal_places=5, default=10000.0)),
                ('az03', models.DecimalField(max_digits=10, decimal_places=5, default=10000.0)),
                ('az04', models.DecimalField(max_digits=10, decimal_places=5, default=10000.0)),
                ('az05', models.DecimalField(max_digits=10, decimal_places=5, default=10000.0)),
                ('az06', models.DecimalField(max_digits=10, decimal_places=5, default=10000.0)),
                ('az07', models.DecimalField(max_digits=10, decimal_places=5, default=10000.0)),
                ('az08', models.DecimalField(max_digits=10, decimal_places=5, default=10000.0)),
                ('az09', models.DecimalField(max_digits=10, decimal_places=5, default=10000.0)),
                ('az10', models.DecimalField(max_digits=10, decimal_places=5, default=10000.0)),
                ('aws01', models.DecimalField(max_digits=10, decimal_places=5, default=10000.0)),
                ('aws02', models.DecimalField(max_digits=10, decimal_places=5, default=10000.0)),
                ('aws03', models.DecimalField(max_digits=10, decimal_places=5, default=10000.0)),
                ('aws04', models.DecimalField(max_digits=10, decimal_places=5, default=10000.0)),
                ('aws05', models.DecimalField(max_digits=10, decimal_places=5, default=10000.0)),
                ('aws06', models.DecimalField(max_digits=10, decimal_places=5, default=10000.0)),
                ('aws07', models.DecimalField(max_digits=10, decimal_places=5, default=10000.0)),
                ('aws08', models.DecimalField(max_digits=10, decimal_places=5, default=10000.0)),
                ('gc01', models.DecimalField(max_digits=10, decimal_places=5, default=10000.0)),
                ('gc02', models.DecimalField(max_digits=10, decimal_places=5, default=10000.0)),
                ('gc03', models.DecimalField(max_digits=10, decimal_places=5, default=10000.0)),
                ('gc04', models.DecimalField(max_digits=10, decimal_places=5, default=10000.0)),
                ('gc05', models.DecimalField(max_digits=10, decimal_places=5, default=10000.0)),
                ('gc06', models.DecimalField(max_digits=10, decimal_places=5, default=10000.0)),
                ('gc07', models.DecimalField(max_digits=10, decimal_places=5, default=10000.0)),
                ('gc08', models.DecimalField(max_digits=10, decimal_places=5, default=10000.0)),
                ('gc09', models.DecimalField(max_digits=10, decimal_places=5, default=10000.0)),
                ('gc10', models.DecimalField(max_digits=10, decimal_places=5, default=10000.0)),
                ('gc11', models.DecimalField(max_digits=10, decimal_places=5, default=10000.0)),
                ('gc12', models.DecimalField(max_digits=10, decimal_places=5, default=10000.0)),
                ('gc13', models.DecimalField(max_digits=10, decimal_places=5, default=10000.0)),
                ('gc14', models.DecimalField(max_digits=10, decimal_places=5, default=10000.0)),
                ('gc15', models.DecimalField(max_digits=10, decimal_places=5, default=10000.0)),
                ('gc16', models.DecimalField(max_digits=10, decimal_places=5, default=10000.0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
