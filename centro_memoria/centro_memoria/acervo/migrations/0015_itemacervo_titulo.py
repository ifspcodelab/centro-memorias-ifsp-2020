# Generated by Django 3.0.7 on 2020-12-07 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acervo', '0014_auto_20201203_1338'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemacervo',
            name='titulo',
            field=models.CharField(default='Campo novo', max_length=100, verbose_name='Título'),
            preserve_default=False,
        ),
    ]
