import requests

from models import DbOpenFoodFacts
from views import View


class App:
    """
    Represent Category table
    """
    def __init__(self):
        self.db = DbOpenFoodFacts()
        self.view = View()

    def save_category(self):
        """
        Save a new category to OFF database.
        """
        r_cat = requests.get('https://fr.openfoodfacts.org/categories&json=1')
        data_json = r_cat.json()
        data_tags = data_json.get('tags')
        data_cat = [data.get('name') for data in data_tags]
        self.db.save_category(data_cat)

    def read(self):
        data = self.db.read_category()
        self.view.display_category(data)

    def save_product(self, categoryId, name):
        """
        Save a new product to OFF database with categoryId.
        """
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
                data.get('nova_group'),
                data.get('url'),
                data.get('stores'),
            )
            lst_product.append(new_product)
            self.db.save_p(new_product)
            productId = self.db.get_product(new_product[0])
            print(productId, categoryId)
            self.db.save_product_category(categoryId, productId)

    def process(self):
        """Get CategoryId and name Product"""
        self.save_category()
        list_tuple = self.db.get_category_id_name()
        for id, name in list_tuple:
            self.save_product(id, name)

    def import_db(self):
        """import db in local by API OFF"""
        choice = int(input("Que souhaitez-vous faire ? \n"
                       "1 - Importer la base de donnée OFF  \n"
                       "2 - Menu Principal \n"
                       "3 - Quitter le programme \n"
                       "Votre choix >  "))
        if choice == 1:
            self.process()
        elif choice == 2:
            pass
        else:
            return exit()

    def scenario(self):
        value = self.view.intro()

        if value == 1:
            cat_id, cat_name = self.view.choose_category(self.db.get_category_id_name())
            print(cat_name)
            prod = self.view.choose_product(self.db.get_product_by_category(cat_id))

            if self.view.save_product(prod):
                self.db.save_product_substitut(prod[0], prod[0])
                print("Votre produit a été sauvegarder dans substitut.")

        elif value == 2:
            lst = self.db.get_substitut()
            f_lst = self.db.get_all_substitute(lst)
            self.view.substitue(f_lst)

        elif value == 3:
            lst = self.db.get_substitut()
            f_lst = self.db.get_all_substitute(lst)
            choice_product = self.view.choose_substitute(f_lst)
            self.db.delete_product_substitute(lst[choice_product][0])
            print(f"Le produit {f_lst[choice_product]} a été supprimé.")

        elif value == 4:
            return exit(0)

        else:
            self.scenario()


def main():
    c = App()
    c.import_db()
    # c.save_product(3153, "pizzas")
    # c.process()
    while True:
        c.scenario()


if __name__ == "__main__":
    main()

