# Generated by Django 4.2 on 2023-10-01 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0006_alter_file_file"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="file",
            name="asset",
        ),
        migrations.AddField(
            model_name="asset",
            name="invoice_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="api.file",
            ),
        ),
    ]