# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-04-02 10:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_auto_20200402_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publish_house',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='myapi.publish_house'),
        ),
    ]
