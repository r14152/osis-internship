# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-03 13:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('internship', '0052_internship_alternate_speciality'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='internshipoffer',
            name='internship',
        ),
    ]
