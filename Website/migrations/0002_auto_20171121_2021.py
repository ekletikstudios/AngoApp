# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-22 01:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='details',
        ),
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
