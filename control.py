# coding: utf-8

import json
import requests
import mysql.connector
from db_off import DbOpenFoodFacts


class Mainproject:
    def __init__(self):
        self.db = DbOpenFoodFacts()

    def get_category(self):
        r_cat = requests.get('https://fr.openfoodfacts.org/categories&json=1')
        data_json = r_cat.json()
        data_tags = data_json.get('tags')
        data_cat = [data.get('name') for data in data_tags]

    # def save_category(self):
    #     r_cat = requests.get('https://fr.openfoodfacts.org/categories&json=1')
    #     data_json = r_cat.json()
    #     data_tags = data_json.get('tags')
    #     data_cat = [data.get('name') for data in data_tags]
    #     self.db.save_category(data_cat)

    def read(self):
        self.db.read_category()

    def updated(self):
        self.db.update_category()

    def deleted(self):
        self.db.delete_category()

    def get_product(self):
        self.keys = [
            "id",
            "product_name",
            "categories",
            "nutrition_grades",
            "ingredients_text",
            "product_url"
        ]

        load_data = {
            'action': 'process',
            'tagtype_0': 'categories',
            'tag_contains_0': 'contains',
            'sort_by': 'unique_scans_n',
            'countries': 'France',
            'json': 1,
            'page': 1
        }

        r_product = requests.get(
            'https://fr.openfoodfacts.org/cgi/search.pl', params=load_data)
        data_json = r_product.json()
        data_tags = data_json.get('products')
        data_products = [data.get("ingredients_text") for data in data_tags]
        print(data_products)


c = Mainproject()
# c.save_category()
# c.updated()
# c.deleted()
print("impression produit")
print(c.get_product())

print(c.read())
