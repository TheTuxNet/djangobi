from datetime import datetime
import pytz
from django.core.management.base import BaseCommand, CommandError
from apps.olist.models import *
from core.settings import BASE_DIR
from pathlib2 import Path
import csv


# Common Conversion Routine ############################################################################################
def xdatetime(s):
    # Ex: 2018-04-18 08:51:30
    format = "%Y-%m-%d %H:%M:%S"
    try:
        dt_obj = datetime.strptime(s, format)
        # dt_obj.tzinfo = pytz.UTC
        return dt_obj
    except:
        return None


def xfloat(s):
    if s is None or str(s).strip() == '':
        return 0
    return float(s)


def xint(s):
    if s is None or str(s).strip() == '':
        return 0
    return int(s)


# Command Management ###################################################################################################
class Command(BaseCommand):
    help = "OLIST Import Data"
    base_path = str(BASE_DIR.parent) + "/dataset/"

    def handle(self, *args, **options):
        # p = Path(self.base_path)
        # for i in p.iterdir():
        #     print(f'*** {i}')

        # self.stdout.write(self.style.SUCCESS(f'*** Sync - product_category_name_translation'))
        # self.sync_category()

        # self.stdout.write(self.style.SUCCESS(f'*** Sync - olist_customers_dataset'))
        # self.sync_customer()

        # self.stdout.write(self.style.SUCCESS(f'*** Sync - olist_products_dataset'))
        # self.sync_product()

        # self.stdout.write(self.style.SUCCESS(f'*** Sync - olist_sellers_dataset'))
        # self.sync_seller()

        # self.stdout.write(self.style.SUCCESS(f'*** Sync - olist_geolocation_dataset'))
        # self.sync_geolocation()

        # self.stdout.write(self.style.SUCCESS(f'*** Sync - olist_orders_dataset'))
        # self.sync_order()

        # self.stdout.write(self.style.SUCCESS(f'*** Sync - olist_order_items_dataset'))
        # self.sync_order_item()

        self.stdout.write(self.style.SUCCESS(f'*** Sync - olist_order_payments_dataset'))
        self.sync_order_payment()


    # Categorie Prodotti ###############################################################################################
    def sync_category(self):
        csv_path = str(self.base_path) + 'product_category_name_translation.csv'
        with open(csv_path, newline='') as csvfile:
            myreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            next(myreader)
            i = 0
            for row in myreader:
                i += 1
                anag = {}
                anag['product_category_name'] = row[0]
                anag['product_category_name_english'] = row[1]
                self.stdout.write(self.style.NOTICE(f'* {i} - {anag}'))
                Category.objects.update_or_create(product_category_name=anag['product_category_name'], defaults=anag)

        # for anag in anags:
        #     self.stdout.write(self.style.NOTICE(f'* {anag}'))
        #     # Category.objects.update_or_create(ext_url=anag['ext_url'], defaults=anag)

    # Anagrafiche Clienti ##############################################################################################
    def sync_customer(self):
        csv_path = str(self.base_path) + 'olist_customers_dataset.csv'
        with open(csv_path, newline='') as csvfile:
            myreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            next(myreader)
            i = 0
            for row in myreader:
                i += 1
                anag = {}
                anag['customer_id'] = row[0]
                anag['customer_unique_id'] = row[1]
                anag['customer_zip_code_prefix'] = row[2]
                anag['customer_city'] = row[3]
                anag['customer_state'] = row[4]
                self.stdout.write(self.style.NOTICE(f'* {i} - {anag}'))
                # Customer.objects.update_or_create(customer_unique_id=anag['customer_unique_id'], defaults=anag)
                Customer.objects.update_or_create(customer_id=anag['customer_id'], defaults=anag)

    # Anagrafiche Prodotti #############################################################################################
    def sync_product(self):
        csv_path = str(self.base_path) + 'olist_products_dataset.csv'
        with open(csv_path, newline='') as csvfile:
            myreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            next(myreader)
            i = 0
            for row in myreader:
                i += 1
                anag = {}
                anag['product_id'] = row[0]
                anag['product_category_name'] = row[1]
                anag['product_name_lenght'] = xint(row[2])
                anag['product_description_lenght'] = xint(row[3])
                anag['product_photos_qty'] = xint(row[4])
                anag['product_weight_g'] = xfloat(row[5])
                anag['product_length_cm'] = xfloat(row[6])
                anag['product_height_cm'] = xfloat(row[7])
                anag['product_width_cm'] = xfloat(row[8])
                self.stdout.write(self.style.NOTICE(f'* {i} - {anag}'))
                Product.objects.update_or_create(product_id=anag['product_id'], defaults=anag)

    # Anagrafiche Venditori ############################################################################################
    def sync_seller(self):
        csv_path = str(self.base_path) + 'olist_sellers_dataset.csv'
        with open(csv_path, newline='') as csvfile:
            myreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            next(myreader)
            i = 0
            for row in myreader:
                i += 1
                anag = {}
                anag['seller_id'] = row[0]
                anag['seller_zip_code_prefix'] = row[1]
                anag['seller_city'] = row[2]
                anag['seller_state'] = row[3]
                self.stdout.write(self.style.NOTICE(f'* {i} - {anag}'))
                Seller.objects.update_or_create(seller_id=anag['seller_id'], defaults=anag)

    # CAP e Coordinate Geografiche #####################################################################################
    def sync_geolocation(self):
        csv_path = str(self.base_path) + 'olist_geolocation_dataset.csv'
        with open(csv_path, newline='') as csvfile:
            myreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            next(myreader)
            i = 0
            for row in myreader:
                i += 1
                anag = {}
                anag['geolocation_zip_code_prefix'] = row[0]
                anag['geolocation_lat'] = xfloat(row[1])
                anag['geolocation_lng'] = xfloat(row[2])
                anag['geolocation_city'] = row[3]
                anag['geolocation_state'] = row[4]
                self.stdout.write(self.style.NOTICE(f'* {i} - {anag}'))
                Geolocation.objects.update_or_create(geolocation_zip_code_prefix=anag['geolocation_zip_code_prefix'],
                                                     defaults=anag)

    def sync_order(self):
        csv_path = str(self.base_path) + 'olist_orders_dataset.csv'
        with open(csv_path, newline='') as csvfile:
            myreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            next(myreader)
            i = 0
            for row in myreader:
                i += 1
                anag = {}
                anag['order_id'] = row[0]
                anag['customer_ref'] = row[1]
                # Getting Customer By Unique ID
                try:
                    customer = Customer.objects.get(customer_id=anag['customer_ref'])
                except Customer.DoesNotExist:
                    customer = None
                anag['customer'] = customer
                anag['order_status'] = row[2]
                anag['order_purchase_timestamp'] = xdatetime(row[3])
                anag['order_approved_at'] = xdatetime(row[4])
                anag['order_delivered_carrier_date'] = xdatetime(row[5])
                anag['order_delivered_customer_date'] = xdatetime(row[6])
                anag['order_estimated_delivery_date'] = xdatetime(row[7])

                self.stdout.write(self.style.NOTICE(f'* {i} - {anag}'))
                Order.objects.update_or_create(order_id=anag['order_id'], defaults=anag)


    def sync_order_item(self):
        csv_path = str(self.base_path) + 'olist_order_items_dataset.csv'
        with open(csv_path, newline='') as csvfile:
            myreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            next(myreader)
            i = 0
            for row in myreader:
                i += 1
                anag = {}
                anag['order_ref'] = row[0]
                try:
                    order = Order.objects.get(order_id=anag['order_ref'])
                except Order.DoesNotExist:
                    order = None
                anag['order'] = order

                anag['order_item_id'] = xint(row[1])


                anag['product_ref'] = row[2]
                try:
                    product = Product.objects.get(product_id=anag['product_ref'])
                except Product.DoesNotExist:
                    product = None
                anag['product'] = product


                anag['seller_ref'] = row[3]
                try:
                    seller = Seller.objects.get(seller_id=anag['seller_ref'])
                except Seller.DoesNotExist:
                    seller = None
                anag['seller'] = seller

                anag['shipping_limit_date'] = xdatetime(row[4])
                anag['price'] = xfloat(row[5])
                anag['freight_value'] = xfloat(row[6])

                self.stdout.write(self.style.NOTICE(f'* {i} - {anag}'))
                OrderItem.objects.update_or_create(order_ref=anag['order_ref'], order_item_id=anag['order_item_id'], defaults=anag)


    def sync_order_payment(self):
        csv_path = str(self.base_path) + 'olist_order_payments_dataset.csv'
        with open(csv_path, newline='') as csvfile:
            myreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            next(myreader)
            i = 0
            for row in myreader:
                i += 1
                anag = {}
                anag['order_ref'] = row[0]
                try:
                    order = Order.objects.get(order_id=anag['order_ref'])
                except Order.DoesNotExist:
                    order = None
                anag['order'] = order

                anag['payment_sequential'] = xint(row[1])
                anag['payment_type'] = row[2]
                anag['payment_installments'] = xint(row[3])
                anag['payment_value'] = xfloat(row[4])

                self.stdout.write(self.style.NOTICE(f'* {i} - {anag}'))
                OrderPayment.objects.update_or_create(order_ref=anag['order_ref'], payment_sequential=anag['payment_sequential'], defaults=anag)