# Generated by Django 2.0 on 2017-12-23 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='abc', unique=True),
        ),
    ]
