# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-18 00:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20161117_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='p_sex',
            field=models.CharField(choices=[('男', '男'), ('女', '女')], default='男', max_length=2),
        ),
    ]