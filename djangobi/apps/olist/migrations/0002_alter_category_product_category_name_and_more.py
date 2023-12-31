# Generated by Django 4.2.5 on 2023-09-11 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_olist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='product_category_name',
            field=models.CharField(blank=True, default='', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.CharField(blank=True, default='', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='geolocation',
            name='geolocation_zip_code_prefix',
            field=models.CharField(blank=True, default='', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(blank=True, default='', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='orderpayment',
            name='order_ref',
            field=models.CharField(blank=True, default='', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.CharField(blank=True, default='', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='seller',
            name='seller_id',
            field=models.CharField(blank=True, default='', max_length=255, unique=True),
        ),
    ]
