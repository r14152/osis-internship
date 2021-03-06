# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-04 04:00
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models

from internship.models.cohort import Cohort
from internship.models.internship_student_information import InternshipStudentInformation


def assign_first_cohort_to_periods(apps, schema_editor):
    cohort = Cohort.objects.first()

    InternshipStudentInformation.objects.all().update(cohort=cohort)


class Migration(migrations.Migration):

    dependencies = [
        ('internship', '0036_cohort_internship_speciality'),
    ]

    operations = [
        migrations.AddField(
            model_name='internshipstudentinformation',
            name='cohort',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='internship.Cohort'),
        ),
        migrations.RunPython(assign_first_cohort_to_periods),
        migrations.AlterField(
            model_name='internshipstudentinformation',
            name='cohort',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='internship.Cohort'),
        )
    ]
