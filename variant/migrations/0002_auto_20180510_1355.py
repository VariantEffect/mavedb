# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-05-10 03:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("variant", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="variant",
            name="modification_date",
            field=models.DateField(
                default=datetime.date.today, verbose_name="Modification date"
            ),
        )
    ]
