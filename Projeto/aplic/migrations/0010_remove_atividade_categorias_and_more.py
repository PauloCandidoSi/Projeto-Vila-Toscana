# Generated by Django 5.1.1 on 2024-10-08 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0009_alter_atividade_capacidade_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atividade',
            name='categorias',
        ),
        migrations.AlterField(
            model_name='atividade',
            name='capacidade',
            field=models.IntegerField(blank=True, help_text='', null=True, verbose_name='Capacidade'),
        ),
    ]
