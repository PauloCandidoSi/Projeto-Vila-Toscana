# Generated by Django 5.1.1 on 2024-10-08 12:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0010_remove_atividade_categorias_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='atividade',
            name='categorias',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aplic.categoria'),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='capacidade',
            field=models.IntegerField(blank=True, help_text='', null=True, verbose_name='Capacidade'),
        ),
    ]
