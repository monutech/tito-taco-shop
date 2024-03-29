# Generated by Django 4.0.5 on 2023-04-11 01:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_total_stock_coupon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='total_stock',
            new_name='general_stock',
        ),
        migrations.AlterField(
            model_name='productattributestock',
            name='attribute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_stock', to='products.attribute'),
        ),
        migrations.AlterField(
            model_name='productattributestock',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attribute_stock', to='products.product'),
        ),
    ]
