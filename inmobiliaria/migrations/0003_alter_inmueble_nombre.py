# Generated by Django 5.0.7 on 2024-07-26 15:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("inmobiliaria", "0002_contactform"),
    ]

    operations = [
        migrations.AlterField(
            model_name="inmueble",
            name="nombre",
            field=models.CharField(max_length=40),
        ),
    ]
