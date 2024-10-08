# Generated by Django 5.1.1 on 2024-10-08 13:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0017_inscricao_atividade_alter_atividade_capacidade_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedback',
            options={'verbose_name': 'FeedBack', 'verbose_name_plural': 'FeedBacks'},
        ),
        migrations.AddField(
            model_name='feedback',
            name='atividade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aplic.atividade'),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='capacidade',
            field=models.IntegerField(blank=True, help_text='', null=True, verbose_name='Capacidade'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='nota',
            field=models.IntegerField(blank=True, default=0, help_text='MAX: 10', null=True, verbose_name='Nota'),
        ),
        migrations.CreateModel(
            name='Notificacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensagem', models.TextField(blank=True, max_length=500, null=True, verbose_name='Mensagem')),
                ('dataEnvio', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('nao_lida', 'Não Lida'), ('lida', 'Lida')], default='nao_lida', max_length=20)),
                ('atividade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aplic.atividade')),
                ('inscricao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplic.inscricao')),
            ],
            options={
                'verbose_name': 'Notificacao',
                'verbose_name_plural': 'Notificacoes',
            },
        ),
    ]
