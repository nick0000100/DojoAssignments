# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 18:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('play_app', '0002_auto_20170818_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='content',
            field=models.TextField(default='This is because I forgot to add parens to content field'),
            preserve_default=False,
        ),
    ]
