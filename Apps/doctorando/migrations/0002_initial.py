# Generated by Django 5.0.6 on 2024-06-12 22:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctorando', '0001_initial'),
        ('programa', '0001_initial'),
        ('sectorest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorando',
            name='programa_idprograma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programa.programa'),
        ),
        migrations.AddField(
            model_name='doctorando',
            name='sectorest_idsectorest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sectorest.sectorest'),
        ),
    ]
