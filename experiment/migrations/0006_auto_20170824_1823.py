# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-24 08:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('experiment', '0005_auto_20170815_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiment',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='exp_created_by_user', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AddField(
            model_name='experiment',
            name='last_edit_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='exp_edited_by_user', to=settings.AUTH_USER_MODEL, verbose_name='Last edited by'),
        ),
        migrations.AddField(
            model_name='experimentset',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='exps_created_by_user', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AddField(
            model_name='experimentset',
            name='last_edit_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='exps_edited_by_user', to=settings.AUTH_USER_MODEL, verbose_name='Last edited by'),
        ),
    ]