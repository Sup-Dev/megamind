# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-03 13:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20180203_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='theme',
            field=models.CharField(default='', max_length=50),
        ),
    ]
