# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-06 20:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perfil',
            old_name='User',
            new_name='ser',
        ),
        migrations.AlterField(
            model_name='perfil',
            name='Bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='fecha_nacimiento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='ocupacion',
            field=models.CharField(blank=True, max_length=140, null=True),
        ),
    ]