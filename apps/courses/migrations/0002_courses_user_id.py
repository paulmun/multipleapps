# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-21 15:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logreg', '0001_initial'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='user_id',
            field=models.ManyToManyField(related_name='courseuser', to='logreg.Users'),
        ),
    ]
