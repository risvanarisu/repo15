# Generated by Django 4.1.7 on 2023-05-16 11:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("reseller", "0006_remove_add_product_status_add_product_reseller_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="add_product",
            name="Status",
            field=models.TextField(db_column="pro_status", max_length=50, null=True),
        ),
    ]
