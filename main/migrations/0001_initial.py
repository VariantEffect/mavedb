# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-23 06:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Licence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_name', models.CharField(default=None, max_length=200, verbose_name='Long name')),
                ('short_name', models.CharField(default=None, max_length=200, verbose_name='Short name')),
                ('legal_code', models.TextField(default=None, verbose_name='Legal Code')),
                ('link', models.URLField(default=None, verbose_name='Link')),
                ('version', models.CharField(default=None, max_length=200, verbose_name='Version')),
            ],
            options={
                'verbose_name': 'Licence',
                'verbose_name_plural': 'Licence',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='default news.')),
                ('date', models.DateField(default=datetime.date.today)),
            ],
            options={
                'verbose_name': 'News item',
                'verbose_name_plural': 'News items',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='SiteInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_about', models.TextField(blank=True, default='')),
                ('_citation', models.TextField(blank=True, default='')),
                ('_usage_guide', models.TextField(blank=True, default='')),
                ('_documentation', models.TextField(blank=True, default='')),
                ('_terms', models.TextField(blank=True, default='')),
                ('_privacy', models.TextField(blank=True, default='')),
                ('_email', models.EmailField(blank=True, default='', max_length=254)),
            ],
            options={
                'verbose_name': 'Site Information',
                'verbose_name_plural': 'Site Information',
            },
        ),
    ]
