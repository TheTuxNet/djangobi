from django.db import models


# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name = "Categoria Prodotto"
        verbose_name_plural = "Categorie Prodotto"

    product_category_name = models.CharField(blank=True, default='', max_length=255, unique=True)
    product_category_name_english = models.CharField(blank=True, default='', max_length=255)


class Customer(models.Model):
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clienti"

        # indexes = [
            # models.Index(fields=['author', 'publication_year'], name='author_pub_year_idx'),
            # models.Index(fields=['customer_id'], name='customer_id_idx'),
        # ]

    customer_id = models.CharField(blank=True, default='', max_length=255, unique=True)
    customer_unique_id = models.CharField(blank=True, default='', max_length=255)
    customer_zip_code_prefix = models.CharField(blank=True, default='', max_length=255)
    customer_city = models.CharField(blank=True, default='', max_length=255)
    customer_state = models.CharField(blank=True, default='', max_length=255)


class Seller(models.Model):
    class Meta:
        verbose_name = "Venditore"
        verbose_name_plural = "Venditori"

    seller_id = models.CharField(blank=True, default='', max_length=255, unique=True)
    seller_zip_code_prefix = models.CharField(blank=True, default='', max_length=255)
    seller_city = models.CharField(blank=True, default='', max_length=255)
    seller_state = models.CharField(blank=True, default='', max_length=255)


class Product(models.Model):
    class Meta:
        verbose_name = "Articolo"
        verbose_name_plural = "Articoli"

    product_id = models.CharField(blank=True, default='', max_length=255, unique=True)
    product_category_name = models.CharField(blank=True, default='', max_length=255)
    product_name_lenght = models.IntegerField(blank=True, default=0)
    product_description_lenght = models.IntegerField(blank=True, default=0)
    product_photos_qty = models.IntegerField(blank=True, default=0)
    product_weight_g = models.FloatField(blank=True, default=0)
    product_length_cm = models.FloatField(blank=True, default=0)
    product_height_cm = models.FloatField(blank=True, default=0)
    product_width_cm = models.FloatField(blank=True, default=0)


class Geolocation(models.Model):
    class Meta:
        verbose_name = "Coordinata GEO"
        verbose_name_plural = "Coordinate GEO"

    geolocation_zip_code_prefix = models.CharField(blank=True, default='', max_length=255, unique=True)
    geolocation_lat = models.FloatField(blank=True, default=0)
    geolocation_lng = models.FloatField(blank=True, default=0)
    geolocation_city = models.CharField(blank=True, default='', max_length=255)
    geolocation_state = models.CharField(blank=True, default='', max_length=255)


class Order(models.Model):
    class Meta:
        verbose_name = "Ordine"
        verbose_name_plural = "Ordini"
        indexes = [
            # models.Index(fields=['author', 'publication_year'], name='author_pub_year_idx'),
            models.Index(fields=['order_status'], name='order_status_idx'),
        ]

    order_id = models.CharField(blank=True, default='', max_length=255, unique=True)
    customer_ref = models.CharField(blank=True, default='', max_length=255)
    customer = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.CASCADE)
    order_status = models.CharField(blank=True, default='', max_length=255)
    order_purchase_timestamp = models.DateTimeField(blank=True, null=True)
    order_approved_at = models.DateTimeField(blank=True, null=True)
    order_delivered_carrier_date = models.DateTimeField(blank=True, null=True)
    order_delivered_customer_date = models.DateTimeField(blank=True, null=True)
    order_estimated_delivery_date = models.DateTimeField(blank=True, null=True)


class OrderItem(models.Model):
    class Meta:
        verbose_name = "Riga Ordine"
        verbose_name_plural = "Righe Ordine"
        indexes = [
            models.Index(fields=['order_ref', 'order_item_id'], name='order_item_idx'),
            # models.Index(fields=['customer_id'], name='customer_id_idx'),
        ]

    order_ref = models.CharField(blank=True, default='', max_length=255)
    order = models.ForeignKey(Order, blank=True, null=True, on_delete=models.CASCADE)

    order_item_id = models.IntegerField(blank=True, default=0)

    product_ref = models.CharField(blank=True, default='', max_length=255)
    product = models.ForeignKey(Product, blank=True, null=True, on_delete=models.CASCADE)

    seller_ref = models.CharField(blank=True, default='', max_length=255)
    seller = models.ForeignKey(Seller, blank=True, null=True, on_delete=models.CASCADE)

    shipping_limit_date = models.DateTimeField(blank=True, null=True)
    price = models.FloatField(blank=True, default=0)
    freight_value = models.FloatField(blank=True, default=0)


class OrderPayment(models.Model):
    class Meta:
        verbose_name = "Pagamento Ordine"
        verbose_name_plural = "Pagamenti Ordine"
        indexes = [
            models.Index(fields=['order_ref', 'payment_sequential'], name='order_seq_payment_idx'),
            # models.Index(fields=['customer_id'], name='customer_id_idx'),
        ]

    order_ref = models.CharField(blank=True, default='', max_length=255)
    order = models.ForeignKey(Order, blank=True, null=True, on_delete=models.CASCADE)

    payment_sequential = models.IntegerField(blank=True, default=0)
    payment_type = models.CharField(blank=True, default='', max_length=255)
    payment_installments = models.IntegerField(blank=True, default=0)
    payment_value = models.FloatField(blank=True, default=0)


