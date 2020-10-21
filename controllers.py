# coding: utf-8

import json
import requests
import mysql.connector
from models import DbOpenFoodFacts
from views import View


class Controller:
    def __init__(self):
        self.db = DbOpenFoodFacts()
        self.view = View()

    def get_category(self):
        r_cat = requests.get('https://fr.openfoodfacts.org/categories&json=1')
        data_json = r_cat.json()
        data_tags = data_json.get('tags')
        data_cat = [data.get('name') for data in data_tags]

    def save_category(self):
        r_cat = requests.get('https://fr.openfoodfacts.org/categories&json=1')
        data_json = r_cat.json()
        data_tags = data_json.get('tags')
        data_cat = [data.get('name') for data in data_tags]
        self.db.save_category(data_cat)

    def read(self):
        data = self.db.read_category()
        self.view.display_category(data)

    def get_product(self):
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

        lst_data = []
        for data in data_tags:
            new_data = (data.get('product_name'), data.get(
                'nutrition_grades'), data.get('ingredients_text'), data.get('nova_groups_tags'), data.get('ingredients'), data.get('product_url'), data.get('magasin'))
            lst_data.append(new_data)
            print(f"{lst_data}  | ")

    def save_product(self, id_category):
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

        lst_product = []
        for data in data_tags:
            new_product = (data.get('product_name'), data.get(
                'nutrition_grades'), data.get('ingredients_text'), data.get('nova_groups_tags'), data.get('ingredients'), data.get('product_url'), data.get('magasin'))
            lst_product.append(new_product[0])
        self.db.save_product(lst_product)


c = Controller()

print("impression produit")
# print(c.get_product())
# print(c.read())
