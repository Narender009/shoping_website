# Generated by Django 5.0.1 on 2024-02-16 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0004_rename_cartiteam_cartitem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='Product',
            new_name='Product_cart',
        ),
    ]
