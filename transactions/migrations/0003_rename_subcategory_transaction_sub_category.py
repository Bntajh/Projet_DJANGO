# Generated by Django 5.0.3 on 2024-04-22 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("transactions", "0002_alter_transaction_label_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="transaction",
            old_name="subcategory",
            new_name="sub_category",
        ),
    ]
