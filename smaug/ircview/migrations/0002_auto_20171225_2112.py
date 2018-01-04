# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-25 21:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ircview', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='logline',
            name='deleted',
            field=models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], db_index=True, default='N', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='logline',
            name='edited',
            field=models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], db_index=True, default='N', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='passed',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='message',
            name='seen',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=1),
        ),
    ]