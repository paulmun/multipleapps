# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-21 15:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_courses_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='user_id',
            field=models.ManyToManyField(to='logreg.Users'),
        ),
    ]
