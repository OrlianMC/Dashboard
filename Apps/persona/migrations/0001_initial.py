# Generated by Django 5.0.6 on 2024-06-11 22:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('area', '0001_initial'),
        ('centro', '0001_initial'),
        ('pais', '0001_initial'),
        ('sectorest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('idpersona', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('ci', models.CharField(max_length=11, unique=True)),
                ('nombre', models.CharField(max_length=45)),
                ('apellido', models.CharField(max_length=45)),
                ('sexo', models.CharField(max_length=45)),
                ('centro_idcentro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centro.centro')),
                ('pais_idpais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pais.pais')),
                ('plantillaarea_idarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='area.area')),
                ('sectorest_idsectorest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sectorest.sectorest')),
            ],
        ),
    ]
