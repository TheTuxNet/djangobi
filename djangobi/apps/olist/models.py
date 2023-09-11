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

    customer_id = models.CharField(blank=True, default='', max_length=255)
    customer_unique_id = models.CharField(blank=True, default='', max_length=255, unique=True)
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

    order_id = models.CharField(blank=True, default='', max_length=255, unique=True)
    customer_ref = models.CharField(blank=True, default='', max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_status = models.CharField(blank=True, default='', max_length=255)
    order_purchase_timestamp = models.DateTimeField(blank=True, default='1001-01-01 00:00:00')
    order_approved_at = models.DateTimeField(blank=True, default='1001-01-01 00:00:00')
    order_delivered_carrier_date = models.DateTimeField(blank=True, default='1001-01-01 00:00:00')
    order_delivered_customer_date = models.DateTimeField(blank=True, default='1001-01-01 00:00:00')
    order_estimated_delivery_date = models.DateTimeField(blank=True, default='1001-01-01 00:00:00')


class OrderItem(models.Model):
    class Meta:
        verbose_name = "Riga Ordine"
        verbose_name_plural = "Righe Ordine"

    order_ref = models.CharField(blank=True, default='', max_length=255)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    order_item_id = models.IntegerField(blank=True, default=0)

    product_ref = models.CharField(blank=True, default='', max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    seller_ref = models.CharField(blank=True, default='', max_length=255)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)

    shipping_limit_date = models.DateTimeField(blank=True, default='1001-01-01 00:00:00')
    price = models.FloatField(blank=True, default=0)
    freight_value = models.FloatField(blank=True, default=0)


class OrderPayment(models.Model):
    class Meta:
        verbose_name = "Pagamento Ordine"
        verbose_name_plural = "Pagamenti Ordine"

    order_ref = models.CharField(blank=True, default='', max_length=255, unique=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    payment_sequential = models.IntegerField(blank=True, default=0)
    payment_type = models.CharField(blank=True, default='', max_length=255)
    payment_installments = models.IntegerField(blank=True, default=0)
    payment_value = models.FloatField(blank=True, default=0)


