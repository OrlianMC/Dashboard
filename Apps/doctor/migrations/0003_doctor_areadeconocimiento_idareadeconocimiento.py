# Generated by Django 5.0.6 on 2024-11-20 14:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('areadeconocimiento', '0002_alter_areadeconocimiento_idareadeconocimiento'),
        ('doctor', '0002_alter_doctor_iddoctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='areadeconocimiento_idareadeconocimiento',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='areadeconocimiento.areadeconocimiento'),
            preserve_default=False,
        ),
    ]