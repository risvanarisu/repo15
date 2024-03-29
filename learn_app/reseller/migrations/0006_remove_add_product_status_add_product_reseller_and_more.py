# Generated by Django 4.1.7 on 2023-05-16 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        (
            "reseller",
            "0005_alter_add_product_price_alter_add_product_quantity_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="add_product",
            name="Status",
        ),
        migrations.AddField(
            model_name="add_product",
            name="reseller",
            field=models.ForeignKey(
                db_column="reseller",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="reseller.reseller",
            ),
        ),
        migrations.AlterField(
            model_name="add_product",
            name="pro_picture",
            field=models.ImageField(
                db_column="pro_pictures", upload_to="product_images/"
            ),
        ),
    ]
