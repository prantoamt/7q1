# Generated by Django 4.1.5 on 2023-01-21 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="name",
            field=models.CharField(max_length=256, unique=True, verbose_name="Name"),
        ),
    ]