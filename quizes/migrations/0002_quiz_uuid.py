# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-11-05 07:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='uuid',
            field=models.CharField(blank=True, max_length=40, null=True, unique=True),
        ),
    ]
