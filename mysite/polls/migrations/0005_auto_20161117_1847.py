# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-17 10:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20161117_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='p_name',
            field=models.CharField(default='template', max_length=100),
        ),
        migrations.AlterField(
            model_name='patient',
            name='p_age',
            field=models.IntegerField(default=0),
        ),
    ]
