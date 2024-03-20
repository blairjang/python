# Generated by Django 5.0.1 on 2024-01-26 00:24

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Burger",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=20)),
                ("price", models.IntegerField(default=0)),
                ("calories", models.IntegerField(default=0)),
            ],
        ),
    ]
