# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-16 09:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_prescription_dispensed'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
