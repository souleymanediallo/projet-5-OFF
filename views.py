import sys


class View:
    def display_category(self, data):
        print("-----------------------------------------------")
        print("| ID | LIST CATEGORIES                        |")
        print("-----------------------------------------------")
        for row in data:
            print(f"| {row[0]}    |   {row[1]}    |")
            print("-----------------------------------------------")
        print("-----------------------------------------------")

    def choose_category(self, category):
        try:
            for i in range(len(category)):
                print(category[i])
            cat = (int(input("Selectionner la categorie \n")),)
        except ValueError:
            print("La valeur choisie n'esst pas la bonne")
            return self.choose_category(category)
        return cat

    def choose_product(self, product):
        try:
            for p in range(len(product)):
                print(product[p])

            prod = (int(input("Selectionner le produit \n")),)
        except ValueError:
            print("La valeur choisie n'est pas la bonne")
            return self.choose_product()
        return prod

    def intro(self):
        try:
            request = int(input(
                "1 - Quel aliment souhaitez-vous remplacer ? \n"
                "2 - Retrouver mes aliments substitués \n"
                "3 - Quitter le programme \n"
                "Votre choix >  "
            ))
            if request not in (1, 2, 3):
                return self.intro()
            return request
        except ValueError:
            return self.intro()

    def substitue(self, lst):
        for i in lst:
            print(i)
