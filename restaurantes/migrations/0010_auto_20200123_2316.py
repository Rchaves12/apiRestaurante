# Generated by Django 3.0.2 on 2020-01-24 02:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantes', '0009_auto_20200123_2310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enderecos',
            name='restaurante',
        ),
        migrations.AddField(
            model_name='restaurantes',
            name='enderecos',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='restaurantes.Enderecos'),
            preserve_default=False,
        ),
    ]
