# Generated by Django 5.0.6 on 2024-06-11 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('idpais', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('codigo', models.CharField(max_length=45)),
            ],
        ),
    ]
