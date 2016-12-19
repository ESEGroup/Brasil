# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-19 15:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20161119_1727'),
    ]

    operations = [
        migrations.CreateModel(
            name='SettingsUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='agendamento',
            name='estado',
            field=models.CharField(choices=[('Agendado', 'Agendado'), ('Cancelado', 'Cancelado'), ('Confirmado', 'Confirmado')], default='Agendado', max_length=12),
        ),
    ]
