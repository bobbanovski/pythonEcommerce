# Generated by Django 2.0 on 2017-12-22 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
