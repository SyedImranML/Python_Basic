# Generated by Django 4.2.8 on 2023-12-08 05:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "online_bs",
            "0004_alter_transaction_amount_alter_transaction_deposit_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="transaction",
            name="reqwithdraw",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
