# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-05 13:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dispenser', '0003_auto_20180605_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='chamber',
            name='name',
            field=models.CharField(default='nothing', max_length=1000),
            preserve_default=False,
        ),
    ]
