# Generated by Django 3.1.2 on 2020-11-28 19:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_auto_20201112_1232'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.UUIDField(default=uuid.uuid4, help_text='Indique el Codigo del producto', primary_key=True, serialize=False)),
                ('nombre_producto', models.CharField(help_text='Ingrese el Nombre del producto', max_length=60)),
                ('precio', models.CharField(help_text='Ingrese el precio del producto', max_length=60)),
                ('marca', models.CharField(help_text='Ingrese la marca del producto', max_length=60)),
            ],
        ),
        migrations.AlterField(
            model_name='compañia',
            name='id_compañia',
            field=models.UUIDField(default=uuid.uuid4, help_text='Indique el Codigo de la Compañia', primary_key=True, serialize=False),
        ),
    ]
