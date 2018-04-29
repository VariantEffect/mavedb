# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-29 01:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('genome', '0001_initial'),
        ('dataset', '0001_initial'),
        ('metadata', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scoreset',
            name='doi_ids',
            field=models.ManyToManyField(blank=True, related_name='associated_scoresets', to='metadata.DoiIdentifier', verbose_name='DOI Identifiers'),
        ),
        migrations.AddField(
            model_name='scoreset',
            name='experiment',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='scoresets', to='dataset.Experiment', verbose_name='Experiment'),
        ),
        migrations.AddField(
            model_name='scoreset',
            name='keywords',
            field=models.ManyToManyField(blank=True, related_name='associated_scoresets', to='metadata.Keyword', verbose_name='Keywords'),
        ),
        migrations.AddField(
            model_name='scoreset',
            name='licence',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='attached_scoresets', to='main.Licence', verbose_name='Licence'),
        ),
        migrations.AddField(
            model_name='scoreset',
            name='modified_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_edited_scoreset', to=settings.AUTH_USER_MODEL, verbose_name='Last edited by'),
        ),
        migrations.AddField(
            model_name='scoreset',
            name='pubmed_ids',
            field=models.ManyToManyField(blank=True, related_name='associated_scoresets', to='metadata.PubmedIdentifier', verbose_name='PubMed Identifiers'),
        ),
        migrations.AddField(
            model_name='scoreset',
            name='replaces',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='replaced_by', to='dataset.ScoreSet', verbose_name='Replaces'),
        ),
        migrations.AddField(
            model_name='scoreset',
            name='sra_ids',
            field=models.ManyToManyField(blank=True, related_name='associated_scoresets', to='metadata.SraIdentifier', verbose_name='SRA Identifiers'),
        ),
        migrations.AddField(
            model_name='experimentset',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_created_experimentset', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AddField(
            model_name='experimentset',
            name='doi_ids',
            field=models.ManyToManyField(blank=True, related_name='associated_experimentsets', to='metadata.DoiIdentifier', verbose_name='DOI Identifiers'),
        ),
        migrations.AddField(
            model_name='experimentset',
            name='keywords',
            field=models.ManyToManyField(blank=True, related_name='associated_experimentsets', to='metadata.Keyword', verbose_name='Keywords'),
        ),
        migrations.AddField(
            model_name='experimentset',
            name='modified_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_edited_experimentset', to=settings.AUTH_USER_MODEL, verbose_name='Last edited by'),
        ),
        migrations.AddField(
            model_name='experimentset',
            name='pubmed_ids',
            field=models.ManyToManyField(blank=True, related_name='associated_experimentsets', to='metadata.PubmedIdentifier', verbose_name='PubMed Identifiers'),
        ),
        migrations.AddField(
            model_name='experimentset',
            name='sra_ids',
            field=models.ManyToManyField(blank=True, related_name='associated_experimentsets', to='metadata.SraIdentifier', verbose_name='SRA Identifiers'),
        ),
        migrations.AddField(
            model_name='experiment',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_created_experiment', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AddField(
            model_name='experiment',
            name='doi_ids',
            field=models.ManyToManyField(blank=True, related_name='associated_experiments', to='metadata.DoiIdentifier', verbose_name='DOI Identifiers'),
        ),
        migrations.AddField(
            model_name='experiment',
            name='experimentset',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='experiments', to='dataset.ExperimentSet', verbose_name='Experiment Set'),
        ),
        migrations.AddField(
            model_name='experiment',
            name='keywords',
            field=models.ManyToManyField(blank=True, related_name='associated_experiments', to='metadata.Keyword', verbose_name='Keywords'),
        ),
        migrations.AddField(
            model_name='experiment',
            name='modified_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_edited_experiment', to=settings.AUTH_USER_MODEL, verbose_name='Last edited by'),
        ),
        migrations.AddField(
            model_name='experiment',
            name='pubmed_ids',
            field=models.ManyToManyField(blank=True, related_name='associated_experiments', to='metadata.PubmedIdentifier', verbose_name='PubMed Identifiers'),
        ),
        migrations.AddField(
            model_name='experiment',
            name='sra_ids',
            field=models.ManyToManyField(blank=True, related_name='associated_experiments', to='metadata.SraIdentifier', verbose_name='SRA Identifiers'),
        ),
        migrations.AddField(
            model_name='experiment',
            name='targets',
            field=models.ManyToManyField(to='genome.TargetGene'),
        ),
    ]
