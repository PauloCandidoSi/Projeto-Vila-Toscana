# Generated by Django 5.1.1 on 2024-10-08 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0013_alter_atividade_capacidade_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atividade',
            name='capacidade',
            field=models.IntegerField(blank=True, help_text='', null=True, verbose_name='Capacidade'),
        ),
    ]
