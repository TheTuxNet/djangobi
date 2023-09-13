# Generated by Django 4.2.5 on 2023-09-12 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_olist', '0009_orderitem_order_item_idx'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='orderitem',
            name='order_item_idx',
        ),
        migrations.AddIndex(
            model_name='orderitem',
            index=models.Index(fields=['order_ref', 'order_item_id'], name='order_item_idx'),
        ),
    ]
