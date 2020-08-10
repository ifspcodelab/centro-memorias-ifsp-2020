# Generated by Django 3.0.7 on 2020-08-06 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('descricao', models.TextField(max_length=250, verbose_name='Descrição do evento')),
                ('destaque', models.BooleanField(verbose_name='Destaque')),
                ('ativo', models.BooleanField(help_text='Este campo indica se este registro já está pronto para aparecer no site publicamente', verbose_name='Registro ativo?')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('atualizado_em', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Evento',
                'verbose_name_plural': 'Eventos',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='FotoEvento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destaque', models.BooleanField(verbose_name='Destaque')),
                ('imagem', models.ImageField(upload_to='', verbose_name='Imagem do Evento')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('atualizado_em', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='fotos', to='eventos.Evento', verbose_name='Evento')),
            ],
            options={
                'verbose_name': 'Foto do Evento',
                'verbose_name_plural': 'Fotos dos Eventos',
                'ordering': ['criado_em'],
            },
        ),
    ]