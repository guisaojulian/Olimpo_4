# Generated by Django 3.2.6 on 2021-09-27 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mantenimiento', '0005_alter_elementomodel_ubicacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elementomodel',
            name='ubicacion',
            field=models.IntegerField(choices=[(0, 'Zona común'), (1, 'Torre 1'), (2, 'Torre 2'), (3, 'Torre 3'), (4, 'Torre 4'), (5, 'Torre 5'), (6, 'Torre 6'), (7, 'Torre 7')]),
        ),
    ]
