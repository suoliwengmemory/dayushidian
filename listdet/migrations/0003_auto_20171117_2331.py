# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 23:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listdet', '0002_auto_20171117_1421'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='List',
            new_name='Post',
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': '详情', 'verbose_name_plural': '详情'},
        ),
    ]
