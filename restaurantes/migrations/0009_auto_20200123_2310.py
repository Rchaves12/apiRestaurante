# Generated by Django 3.0.2 on 2020-01-24 02:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantes', '0008_auto_20200123_2250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurantes',
            name='enderecos',
        ),
        migrations.AddField(
            model_name='enderecos',
            name='restaurante',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='restaurantes.Restaurantes'),
            preserve_default=False,
        ),
    ]
