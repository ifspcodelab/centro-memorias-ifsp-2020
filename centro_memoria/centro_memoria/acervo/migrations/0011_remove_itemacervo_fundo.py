# Generated by Django 3.0.7 on 2020-11-30 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acervo', '0010_auto_20201130_1237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemacervo',
            name='fundo',
        ),
    ]