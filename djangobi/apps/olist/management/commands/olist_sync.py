from django.core.management.base import BaseCommand, CommandError
from apps.olist.models import *
from core.settings import BASE_DIR
from pathlib2 import Path
import csv


# Command Management ##############################################################################
class Command(BaseCommand):
    help = "OLIST Import Data"
    base_path = str(BASE_DIR.parent) + "/dataset/"

    def handle(self, *args, **options):
        # p = Path(self.base_path)
        # for i in p.iterdir():
        #     print(f'*** {i}')

        self.stdout.write(self.style.SUCCESS(f'*** Sync - product_category_name_translation'))
        self.sync_category()

        self.stdout.write(self.style.SUCCESS(f'*** Sync - olist_customers_dataset'))
        self.sync_customer()


    # Categorie Prodotti ###############################################################################################
    def sync_category(self):
        csv_path = str(self.base_path) + 'product_category_name_translation.csv'
        with open(csv_path, newline='') as csvfile:
            myreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            next(myreader)

            for row in myreader:
                anag = {}
                anag['product_category_name'] = row[0]
                anag['product_category_name_english'] = row[1]
                self.stdout.write(self.style.NOTICE(f'* {anag}'))
                Category.objects.update_or_create(product_category_name=anag['product_category_name'], defaults=anag)


        # for anag in anags:
        #     self.stdout.write(self.style.NOTICE(f'* {anag}'))
        #     # Category.objects.update_or_create(ext_url=anag['ext_url'], defaults=anag)


    def sync_customer(self):
        csv_path = str(self.base_path) + 'olist_customers_dataset.csv'
        with open(csv_path, newline='') as csvfile:
            myreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            next(myreader)

            for row in myreader:
                anag = {}
                anag['customer_id'] = row[0]
                anag['customer_unique_id'] = row[1]
                anag['customer_zip_code_prefix'] = row[2]
                anag['customer_city'] = row[3]
                anag['customer_state'] = row[4]
                self.stdout.write(self.style.NOTICE(f'* {anag}'))
                Customer.objects.update_or_create(customer_unique_id=anag['customer_unique_id'], defaults=anag)


        # for anag in anags:
        #     self.stdout.write(self.style.NOTICE(f'* {anag}'))
        #     # Category.objects.update_or_create(ext_url=anag['ext_url'], defaults=anag)


