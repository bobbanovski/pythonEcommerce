# Generated by Django 2.0 on 2017-12-23 11:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20171223_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
