# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-10 03:47
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import scoreset.validators


class Migration(migrations.Migration):

    dependencies = [
        ('scoreset', '0003_scoreset_keywords'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scoreset',
            name='dataset_columns',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'counts': ['count'], 'scores': ['hgvs', 'score', 'se']}, validators=[scoreset.validators.valid_scoreset_json], verbose_name='Dataset columns'),
        ),
        migrations.AlterField(
            model_name='scoreset',
            name='doi_id',
            field=models.CharField(blank=True, default='', max_length=256, verbose_name='DOI identifier'),
        ),
        migrations.AlterField(
            model_name='variant',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'counts': {'count': [None], 'hgvs': [None]}, 'scores': {'hgvs': [None], 'score': [None], 'se': [None]}}, validators=[scoreset.validators.valid_variant_json], verbose_name='Data columns'),
        ),
    ]
