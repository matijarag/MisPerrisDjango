# Generated by Django 2.1.2 on 2018-10-22 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Perris', '0003_auto_20181022_2038'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='foto',
            field=models.ImageField(default='hola', upload_to=''),
        ),
    ]