# Generated by Django 4.1.7 on 2023-04-18 08:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("reseller", "0002_reseller_user_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reseller",
            name="user_id",
            field=models.IntegerField(db_column="login_id", null=True),
        ),
    ]