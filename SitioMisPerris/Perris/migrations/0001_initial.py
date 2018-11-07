# Generated by Django 2.1.2 on 2018-11-07 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id_mascota', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(default='null', max_length=40)),
                ('raza_predominante', models.CharField(default='null', max_length=40)),
                ('descripcion', models.CharField(default='null', max_length=50)),
                ('estado', models.IntegerField(choices=[(1, 'Rescatado'), (2, 'Disponible'), (3, 'Adoptado')], default=1)),
                ('foto', models.ImageField(blank=True, upload_to='Perris/')),
            ],
        ),
    ]
