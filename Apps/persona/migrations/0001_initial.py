# Generated by Django 5.0.6 on 2024-06-11 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idpersona', models.IntegerField(auto_created=True)),
                ('ci', models.CharField(max_length=11)),
                ('nombre', models.CharField(max_length=45)),
                ('apellido', models.CharField(max_length=45)),
                ('sexo', models.CharField(max_length=45)),
            ],
        ),
    ]