# Generated by Django 3.0.7 on 2020-11-25 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acervo', '0006_auto_20201125_1208'),
    ]

    operations = [
        migrations.RenameField(
            model_name='atividadeevento',
            old_name='especificação',
            new_name='especificacao',
        ),
    ]