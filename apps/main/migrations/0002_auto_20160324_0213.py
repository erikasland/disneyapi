# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-24 02:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='curr_time',
            field=models.BigIntegerField(),
        ),
    ]
