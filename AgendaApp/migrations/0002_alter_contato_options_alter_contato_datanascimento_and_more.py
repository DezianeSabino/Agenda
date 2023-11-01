# Generated by Django 4.2.7 on 2023-11-01 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AgendaApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contato',
            options={'verbose_name': 'Pessoa', 'verbose_name_plural': 'Pessoas'},
        ),
        migrations.AlterField(
            model_name='contato',
            name='DataNascimento',
            field=models.DateField(verbose_name='Data de Nascença'),
        ),
        migrations.AlterField(
            model_name='contato',
            name='nome',
            field=models.CharField(max_length=200),
        ),
    ]
