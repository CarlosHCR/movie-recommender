# Generated by Django 5.0.6 on 2024-07-16 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.TextField(verbose_name='Genre'),
        ),
    ]
