# Generated by Django 5.1 on 2024-08-29 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fintehtest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
