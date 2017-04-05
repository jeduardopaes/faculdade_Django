# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 21:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_auto_20170401_0025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Roupa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('tamanho', models.CharField(max_length=15)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=20)),
                ('cor', models.CharField(max_length=25)),
                ('tipo', models.CharField(max_length=15)),
                ('descricao', models.CharField(max_length=15)),
            ],
        ),
    ]