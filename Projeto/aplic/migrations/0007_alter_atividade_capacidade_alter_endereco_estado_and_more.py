# Generated by Django 5.1.1 on 2024-10-08 12:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0006_residente_alter_atividade_capacidade_endereco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atividade',
            name='capacidade',
            field=models.IntegerField(blank=True, help_text='', null=True, verbose_name='Capacidade'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='estado',
            field=models.CharField(blank=True, choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], help_text='Formato AA', max_length=2, verbose_name='UF'),
        ),
        migrations.CreateModel(
            name='Responsavel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefone', models.CharField(blank=True, help_text='Formato (00) 0000-0000', max_length=20, verbose_name='Telefone')),
                ('celular', models.CharField(blank=True, help_text='Formato (00) 00000-0000', max_length=20, verbose_name='Celular')),
                ('telefone_comercial', models.CharField(blank=True, help_text='Formato 00) 0000-0000', max_length=20, verbose_name='Tel. Comercial')),
                ('administador', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='aplic.administrador')),
                ('residentes', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='aplic.residente')),
            ],
            options={
                'verbose_name': 'Responsável',
                'verbose_name_plural': 'Responsáveis',
            },
        ),
    ]
