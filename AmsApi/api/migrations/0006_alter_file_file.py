# Generated by Django 4.2 on 2023-10-01 13:21

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0005_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="file",
            name="file",
            field=models.FileField(
                blank=True, null=True, upload_to=api.models.upload_to
            ),
        ),
    ]
