import json
import requests

from models import DbOpenFoodFacts
from views import View


class App:
    def __init__(self):
        self.db = DbOpenFoodFacts()
        self.view = View()

    def get_category(self):
        """Get url for data API"""
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

        r_product = requests.get('https://fr.openfoodfacts.org/cgi/search.pl', params=load_data)
        data_json = r_product.json()
        data_tags = data_json.get('products')

        #print("Product Name \t\t\t Nutrition Grade \t\t\t\t Ingredients")
        lst_data = []
        for data in data_tags:
            new_data = (
                data.get('product_name'),
                data.get('nutrition_grades'),
                data.get('ingredients_text'),
                data.get('nova_groups_tags'),
                data.get('ingredients'),
                data.get('product_url'),
                data.get('magasin'),
            )
            lst_data.append(new_data)

    def save_product(self, categoryId, name):
        load_data = {
            'action': 'process',
            'tagtype_0': 'categories',
            'tag_contains_0': 'contains',
            'sort_by': 'unique_scans_n',
            'countries': 'France',
            'json': 1,
            'page': 1,
            'tag_0': name,
        }

        r_product = requests.get('https://fr.openfoodfacts.org/cgi/search.pl', params=load_data)
        data_json = r_product.json()
        data_tags = data_json.get('products')

        lst_product = []
        for data in data_tags[:50]:
            new_product = (
                data.get('product_name'),
                data.get('nutrition_grades'),
                data.get('ingredients_text'),
                data.get('nova_groups_tags'),
                data.get('ingredients'),
                data.get('product_url'),
                data.get('magasin'),
            )
            lst_product.append(new_product)
            # créer la méthode # sauvegarger un produit et retour id
            self.db.save_p(new_product)
            productId = self.db.get_product(new_product[0])
            print(productId, categoryId)
            self.db.save_product_category(categoryId, productId)  # sauvegarder

    def process(self):
        self.save_category()
        list_tuple = self.db.get_category_id_name()
        # récuper id et nom produit
        for id, name in list_tuple:
            self.save_product(id, name)

# TODO : RECUPERER LE NOM DE LA CATEGORIE AU LIEU DE L'ID LIGNE 106

    def scenario(self):
        value = self.view.intro()
        if value == 1:
            cat_id = self.view.choose_category(self.db.get_category_id_name())
            prod_id = self.view.choose_product(self.db.get_product_by_category(cat_id[0]))
            self.view.product_views(self.db.get_product())

        if value == 2:
            lst = self.db.get_category_id_name()
            self.view.substitue(lst)

# TODO : VÉRIFIFER L'AFFICHAGE get_product_by_category RECUPERR LE RETOUR DE LUTILISATEUR ET SAUVEGARDE EN BASE
# TODO : METHODE ET RETOUR DE METHODE POUR SAUVEGARDER LE PRODUIT
# TODO : CRÉER UNE METHODE DANS APP ET DANS MODELS POUR SAUVEGARDER LE CHOIX DE L'UTILISATEUR

def main():
    c = App()
    #c.get_product()
    #c.process()
    c.scenario()


if __name__ == "__main__":
    main()
