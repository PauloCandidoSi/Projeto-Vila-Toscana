<<<<<<< HEAD
# Generated by Django 5.1.1 on 2024-10-08 11:52
=======
# Generated by Django 5.1.1 on 2024-10-01 22:30
>>>>>>> 3b271dcb329285b93f5416045b9ce35c5e089e73

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0004_atividade_evento_alter_atividade_capacidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atividade',
            name='capacidade',
            field=models.IntegerField(blank=True, help_text='', null=True, verbose_name='Capacidade'),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='evento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Evento', to='aplic.evento'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='nome',
            field=models.CharField(blank=True, max_length=100, verbose_name='Nome'),
        ),
    ]
