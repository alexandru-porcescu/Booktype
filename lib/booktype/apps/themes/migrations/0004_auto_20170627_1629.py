# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-06-27 16:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('themes', '0003_data_migrate_theme'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usertheme',
            name='book',
        ),
        migrations.RemoveField(
            model_name='usertheme',
            name='owner',
        ),
        migrations.DeleteModel(
            name='UserTheme',
        ),
    ]