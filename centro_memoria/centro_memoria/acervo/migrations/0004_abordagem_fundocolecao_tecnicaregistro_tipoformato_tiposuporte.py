# Generated by Django 3.0.7 on 2020-11-23 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acervo', '0003_auto_20201119_1412'),
    ]

    operations = [
        migrations.CreateModel(
            name='Abordagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100, verbose_name='Tipo')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('atualizado_em', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Abordagem',
                'verbose_name_plural': 'Abordagens',
                'ordering': ['criado_em'],
            },
        ),
        migrations.CreateModel(
            name='FundoColecao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('atualizado_em', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Fundo/Coleção',
                'verbose_name_plural': 'Fundos/Coleções',
                'ordering': ['criado_em'],
            },
        ),
        migrations.CreateModel(
            name='TecnicaRegistro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('atualizado_em', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Técnica de Registro',
                'verbose_name_plural': 'Técnicas de Registro',
                'ordering': ['criado_em'],
            },
        ),
        migrations.CreateModel(
            name='TipoFormato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('atualizado_em', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Tipo de Formato',
                'verbose_name_plural': 'Tipos de Formato',
                'ordering': ['criado_em'],
            },
        ),
        migrations.CreateModel(
            name='TipoSuporte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('atualizado_em', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Tipo de Suporte',
                'verbose_name_plural': 'Tipos de Suporte',
                'ordering': ['criado_em'],
            },
        ),
    ]
