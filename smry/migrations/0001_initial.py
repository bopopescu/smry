# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('chart_type', models.CharField(max_length=10)),
                ('feature', models.CharField(max_length=10)),
                ('rgn_name', models.CharField(max_length=40)),
                ('years', models.CharField(max_length=100)),
                ('img_size', models.CharField(max_length=10)),
                ('image_filename', models.CharField(max_length=120)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Legend',
            fields=[
                ('key', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('short_name', models.CharField(max_length=60)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('feature', models.CharField(max_length=10)),
                ('rgn_name', models.CharField(max_length=40)),
                ('year', models.CharField(max_length=4)),
                ('rsl', models.CharField(max_length=10)),
                ('img_size', models.CharField(max_length=10)),
                ('image_filename', models.CharField(max_length=120)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('region', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=40)),
                ('short_name', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SiteVars',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('crnt_year', models.CharField(default=b'2010', max_length=4)),
                ('crnt_rgn', models.CharField(default=b'USA48', max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TextItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField()),
                ('view', models.CharField(max_length=80)),
                ('name', models.CharField(max_length=40)),
                ('title', models.CharField(max_length=250)),
                ('text', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='map',
            name='region',
            field=models.ForeignKey(to='smry.Region'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='chart',
            name='region',
            field=models.ForeignKey(to='smry.Region'),
            preserve_default=True,
        ),
    ]
