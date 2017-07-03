# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-23 20:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo_inicio', models.DateTimeField()),
                ('periodo_fim', models.DateTimeField()),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Questao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enunciado', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.IntegerField()),
                ('atualizado_em', models.DateTimeField(auto_now_add=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('avaliacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avaliacoes', to='testes.Avaliacao')),
                ('questao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questoes', to='testes.Questao')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('nome_usuario', models.CharField(max_length=25)),
                ('funcao', models.CharField(choices=[('O', 'Operador'), ('A', 'Administrador')], max_length=1)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='resposta',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuarios', to='testes.Usuario'),
        ),
        migrations.AddField(
            model_name='avaliacao',
            name='questoes',
            field=models.ManyToManyField(to='testes.Questao'),
        ),
    ]
