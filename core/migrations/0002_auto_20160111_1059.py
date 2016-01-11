# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-11 09:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgrammeManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='offeryearcalendar',
            name='offer_year',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.OfferYear'),
        ),
        migrations.AlterField(
            model_name='structure',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AddField(
            model_name='programmemanager',
            name='faculty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Structure'),
        ),
        migrations.AddField(
            model_name='programmemanager',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Person'),
        ),
    ]
