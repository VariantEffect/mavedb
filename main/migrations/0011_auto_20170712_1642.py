# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-12 06:42
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20170712_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiment',
            name='base_coverage',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='num_variants',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='read_depth',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
