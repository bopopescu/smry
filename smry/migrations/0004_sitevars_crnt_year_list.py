# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smry', '0003_geodataattrs'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitevars',
            name='crnt_year_list',
            field=models.CharField(default=b'2010', max_length=256),
            preserve_default=True,
        ),
    ]
