# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-09 08:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20160122_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
