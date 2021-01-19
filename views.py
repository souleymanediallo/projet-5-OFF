class View:
    """Get view"""
    def choose_category(self, category):
        print("--------------- LISTE DES CATEGORIES ----------------------")
        tmp_values = {}
        for index, cat_tuple in enumerate(category[:10]):
            tmp_index = index + 1
            tmp_values[tmp_index] = cat_tuple
            print(f"{tmp_index} - {cat_tuple[1]}")
        try:
            choice = int(input("choisir le numéro de votre categorie : > "))
        except Exception as e:
            pass
        return tmp_values.get(choice)

    def choose_product(self, product):
        print("--------------- LISTE DES PRODUITS ----------------------")
        for i, p in enumerate(product):
            print(f"{i+1} - {p[1]} - {p[2]} - {p[3]}")
        try:
            choice = int(input("Choisir le numéro de votre produit : > "))
            prod = product[choice - 1]
        except (ValueError, IndexError):
            print("La valeur choisie n'est pas la bonne")
            return exit()
        return prod

    def intro(self):
        print("--------------- MENU PRINCIPAL ----------------------")
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
        print("--------------- ALIMENTS SUBSTITUTÉS ----------------------")
        for index, name in enumerate(lst):
            print(f"{index + 1} - {name}")

    def save_product(self, prod):
        print("--------------- PRODUIT SUBSTITUTÉ ----------------------")
        print(f"{prod}")
        print("Que souhaitez-vous faire ?")
        choice = input(
            "oui - Sauvegarder le produit dans mes subsituts \n"
            "non - Quitter le programme \n"
            "Votre choix > ").lower()
        if choice == "oui":
            return True
        return False





