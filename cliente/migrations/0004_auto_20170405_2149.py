# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 21:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_roupa'),
    ]

    operations = [
        migrations.AddField(
            model_name='roupa',
            name='situacao',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='roupa',
            name='descricao',
            field=models.TextField(),
        ),
    ]
