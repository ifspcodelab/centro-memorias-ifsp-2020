# Generated by Django 3.0.7 on 2020-12-09 06:16

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acontecimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Título do acontecimento')),
                ('descricao', ckeditor.fields.RichTextField(max_length=200, verbose_name='Descrição ')),
                ('sobre', ckeditor.fields.RichTextField(verbose_name='Descrição longa')),
                ('data', models.DateField(verbose_name='Data do acontecimento')),
                ('ativo', models.BooleanField(help_text='Este campo indica se este registro já está pronto para aparecer no site publicamente', verbose_name='Registro ativo?')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('atualizado_em', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Acontecimento da Linha do Tempo',
                'verbose_name_plural': 'Acontecimentos da Linha do Tempo',
                'ordering': ['titulo'],
            },
        ),
        migrations.CreateModel(
            name='LinhaDoTempo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Título da linha do tempo')),
                ('descricao', ckeditor.fields.RichTextField(max_length=200, verbose_name='Descrição curta')),
                ('descricao_longa', ckeditor.fields.RichTextField(verbose_name='Descrição longa')),
                ('inicio_periodo', models.DateField(verbose_name='Inicío dessa linha do tempo')),
                ('fim_periodo', models.DateField(verbose_name='Fim dessa linha do tempo')),
                ('image', models.ImageField(upload_to='', verbose_name='Imagem capa')),
                ('ativo', models.BooleanField(help_text='Este campo indica se este registro já está pronto para aparecer no site publicamente', verbose_name='Registro ativo?')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('atualizado_em', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Linha do Tempo',
                'verbose_name_plural': 'Linhas do tempo',
                'ordering': ['inicio_periodo'],
            },
        ),
        migrations.CreateModel(
            name='FotoAcontecimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='nome da imagem')),
                ('destaque', models.BooleanField(verbose_name='Destaque')),
                ('imagem', models.ImageField(upload_to='', verbose_name='Imagem do Acontecimento')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('atualizado_em', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('acontecimento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='fotos', to='linha_tempo.Acontecimento', verbose_name='Acontecimento')),
            ],
            options={
                'verbose_name': 'Foto do Acontecimento',
                'verbose_name_plural': 'Fotos dos Acontecimentos',
                'ordering': ['criado_em'],
            },
        ),
        migrations.AddField(
            model_name='acontecimento',
            name='linha_do_tempo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='acontecimento', to='linha_tempo.LinhaDoTempo', verbose_name='Linha do Tempo'),
        ),
    ]
