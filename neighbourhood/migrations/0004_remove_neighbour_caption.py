# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-31 12:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourhood', '0003_auto_20191031_1213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='neighbour',
            name='caption',
        ),
    ]
