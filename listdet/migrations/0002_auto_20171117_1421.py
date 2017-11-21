# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 14:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listdet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10, verbose_name='类别')),
                ('title', models.CharField(max_length=30, verbose_name='标题')),
                ('image', models.ImageField(upload_to='fengmian/%Y/%m', verbose_name='封面')),
                ('url', models.URLField(verbose_name='访问地址')),
                ('index', models.IntegerField(default=100, verbose_name='顺序')),
                ('author', models.CharField(max_length=10, verbose_name='作者')),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '列表',
                'verbose_name_plural': '列表',
            },
        ),
        migrations.DeleteModel(
            name='Csslist',
        ),
        migrations.DeleteModel(
            name='H5list',
        ),
        migrations.DeleteModel(
            name='Jslist',
        ),
    ]