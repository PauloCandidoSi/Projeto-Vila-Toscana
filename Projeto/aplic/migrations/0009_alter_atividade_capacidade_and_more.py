# Generated by Django 5.1.1 on 2024-10-08 12:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0008_categoria_alter_atividade_capacidade_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atividade',
            name='capacidade',
            field=models.IntegerField(blank=True, help_text='', null=True, verbose_name='Capacidade'),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='categorias',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='aplic.categoria'),
        ),
    ]
