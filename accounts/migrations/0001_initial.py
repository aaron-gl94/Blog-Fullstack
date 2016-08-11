# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-06 20:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_nacimiento', models.DateField()),
                ('ocupacion', models.CharField(max_length=140)),
                ('genero', models.CharField(choices=[('H', 'Hombre'), ('M', 'Mujer')], default='M', max_length=140)),
                ('Bio', models.TextField()),
                ('Civil', models.CharField(choices=[('S', 'Soltero'), ('C', 'Casado')], default='S', max_length=140)),
                ('User', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]