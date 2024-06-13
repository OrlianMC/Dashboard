# Generated by Django 5.0.6 on 2024-06-13 00:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctor', '0001_initial'),
        ('doctorando', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('idtutor', models.IntegerField(primary_key=True, serialize=False)),
                ('doctor_iddoctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor')),
                ('doctorando_iddoctorando', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctorando.doctorando')),
            ],
        ),
    ]
