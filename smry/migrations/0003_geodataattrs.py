# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smry', '0002_sitevars_dscrpt_txt'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeoDataAttrs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_id', models.CharField(max_length=20)),
                ('years', models.CharField(max_length=256)),
                ('descr', models.CharField(max_length=512)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
