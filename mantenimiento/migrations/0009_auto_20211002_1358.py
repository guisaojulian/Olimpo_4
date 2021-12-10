# Generated by Django 3.2.6 on 2021-10-02 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edificios', '0006_alter_presupuesto_rubro_frecuencia'),
        ('mantenimiento', '0008_alter_correctivomodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elementomodel',
            name='edificio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edificios.edificio_model'),
        ),
        migrations.CreateModel(
            name='OtModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateField(auto_now=True)),
                ('prioridad', models.BigIntegerField(choices=[{0, 'Alta'}, {1, 'Baja'}])),
                ('requerido', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=200)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('observaciones', models.CharField(max_length=200)),
                ('elemento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mantenimiento.elementomodel')),
            ],
        ),
    ]