# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-22 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repertoire', '0007_auto_20170921_2015'),
    ]

    operations = [
        migrations.AddField(
            model_name='oeuvre',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='oeuvre',
            name='id_zotero',
            field=models.CharField(db_index=True, max_length=200),
        ),
    ]
