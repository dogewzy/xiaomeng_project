# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-19 10:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('polls', '0006_auto_20161118_0823'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnose',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_num', models.IntegerField(default=0)),
                ('prescription', models.TextField(default='')),
                ('result', models.TextField(default='')),
                ('time', models.TimeField(default=datetime.datetime(2016, 11, 19, 10, 42, 31, 825288, tzinfo=utc))),
                ('man', models.CharField(default='临时', max_length=10)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Patient')),
            ],
        ),
    ]
