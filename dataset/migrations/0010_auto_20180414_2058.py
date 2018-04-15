# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-14 10:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0009_auto_20180414_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scoreset',
            name='target',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='scoresets', to='genome.TargetGene', verbose_name='Target gene'),
        ),
    ]
