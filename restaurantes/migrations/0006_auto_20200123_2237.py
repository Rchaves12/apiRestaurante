# Generated by Django 3.0.2 on 2020-01-24 01:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantes', '0005_auto_20200123_2235'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enderecos',
            old_name='logradouro',
            new_name='enderecos',
        ),
        migrations.RenameField(
            model_name='restaurantes',
            old_name='endereco',
            new_name='enderecos',
        ),
    ]
