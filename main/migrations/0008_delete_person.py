# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-11 06:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_person'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
    ]