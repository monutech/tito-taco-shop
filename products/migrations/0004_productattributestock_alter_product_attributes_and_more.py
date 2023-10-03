# Generated by Django 4.0.5 on 2023-04-02 22:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_category_remove_product_attribute_bases_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductAttributeStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.IntegerField(blank=True, default=None, null=True)),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.attribute')),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='attributes',
        ),
        migrations.AddField(
            model_name='product',
            name='attributes',
            field=models.ManyToManyField(through='products.ProductAttributeStock', to='products.attribute'),
        ),
        migrations.AddField(
            model_name='productattributestock',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
    ]