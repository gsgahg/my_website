# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-13 18:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20160313_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]
