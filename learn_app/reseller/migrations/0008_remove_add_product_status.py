# Generated by Django 4.1.7 on 2023-05-16 11:43

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("reseller", "0007_add_product_status"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="add_product",
            name="Status",
        ),
    ]
