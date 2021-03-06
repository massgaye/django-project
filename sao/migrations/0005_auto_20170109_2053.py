# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-09 20:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sao', '0004_auto_20170109_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personne',
            name='DateSignalement',
            field=models.DateTimeField(verbose_name='Date et heure du signalement'),
        ),
        migrations.AlterField(
            model_name='personne',
            name='Nom',
            field=models.CharField(max_length=50, verbose_name='Nom de la personne'),
        ),
        migrations.AlterField(
            model_name='personne',
            name='StructureAcceuil',
            field=models.CharField(choices=[('venu avec sa mère', 'venu avec sa mère'), ('SAO', 'SAO'), ('AEMO', 'AEMO'), ('Famille', 'Famille'), ('communauté', 'communauté'), ('né à la Maison rose', 'né à la Maison rose'), ("forces de l' ordre", "forces de l'ordre"), ('structures sanitaires', 'structures sanitaires'), ('partenaires sociaux', 'partenaires sociaux'), ('pouponnière', 'pouponnière'), ('médias', 'médias'), ("venu d'elle/de lui-même", "venu d'elle/de lui-même"), ('autres', 'autres')], default='SAO', max_length=50, verbose_name="Structure d'acceuil"),
        ),
        migrations.AlterField(
            model_name='personne',
            name='SuiviInfo',
            field=models.CharField(max_length=100, verbose_name='Informations de suivi'),
        ),
        migrations.AlterField(
            model_name='personne',
            name='TypeSignalement',
            field=models.CharField(choices=[('Direct', 'Direct'), ('Téléphone', 'Téléphone'), ('déclaration de recherche', 'déclaration de recherche')], default='Direct', max_length=50, verbose_name='Type de signalement'),
        ),
    ]
