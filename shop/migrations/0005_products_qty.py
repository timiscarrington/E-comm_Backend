# Generated by Django 4.1.5 on 2023-01-31 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_products_image2'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='qty',
            field=models.FloatField(default=0),
        ),
    ]