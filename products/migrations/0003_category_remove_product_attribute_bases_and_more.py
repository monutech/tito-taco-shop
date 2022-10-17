# Generated by Django 4.0.5 on 2022-10-05 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_attributebase_alter_product_image_attribute_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='attribute_bases',
        ),
        migrations.AlterField(
            model_name='attribute',
            name='internal_value',
            field=models.CharField(max_length=75),
        ),
        migrations.AlterField(
            model_name='attribute',
            name='value',
            field=models.CharField(max_length=75),
        ),
        migrations.AlterField(
            model_name='attributebase',
            name='name',
            field=models.CharField(max_length=75),
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.CharField(max_length=1000)),
                ('category', models.ManyToManyField(blank=True, null=True, to='products.category')),
            ],
        ),
    ]