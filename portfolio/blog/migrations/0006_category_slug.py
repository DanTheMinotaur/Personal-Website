# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-21 21:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170712_1949'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]