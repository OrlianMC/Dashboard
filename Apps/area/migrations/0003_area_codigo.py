# Generated by Django 5.0.6 on 2024-11-20 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('area', '0002_alter_area_idarea'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='codigo',
            field=models.CharField(default='new row', max_length=45),
        ),
    ]
