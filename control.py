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
        data_cat = [data_tags.get('name')]

    def save_category(self):
        r_cat = requests.get(
            'https://fr.openfoodfacts.org/categories&json=1')
        data_json = r_cat.json()
        data_tags = data_json.get('tags')
        data_cat = [data_tags.get('name') for d in data_tags]
        self.db.save_category(data_cat)

    def read(self):
        pass

    def updated(self):
        pass

    def test(self):
        self.save_category()


c = Mainproject()
c.test()
