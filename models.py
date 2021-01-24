import mysql.connector


class DbOpenFoodFacts:
    """
    Connect db local, save category, save product
    """
    CATEGORY_SIZE = 11
    PRODUCT_SIZE = 51

    def __init__(self):
        self.db = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='rootroot',
            auth_plugin='mysql_native_password',
            database='db_sql',
            charset='utf8')
        self.cursor = self.db.cursor()

    def save_category(self, lst_category):
        for i in range(1, self.CATEGORY_SIZE):
            add_category = ("INSERT INTO Category (name) VALUES (%s)")
            self.cursor.execute(add_category, (lst_category[i],))
            self.db.commit()

    def save_p(self, lst_product):
        add_product = ("INSERT INTO Product (product_name, nutrition_grades, ingredients_text, nova_group,"
                       "url, stores) VALUES (%s, %s, %s, %s, %s, %s)")

        tuple_data = (lst_product[0],
                      lst_product[1],
                      lst_product[2][:50],
                      lst_product[3],
                      lst_product[4],
                      lst_product[5],
                      )
        if isinstance(tuple_data, tuple):
            print(tuple_data)

        self.cursor.execute(add_product, tuple_data)
        self.db.commit()

    def save_product_category(self, categoryId, productId):
        project_data = (categoryId, productId)
        self.cursor.execute("INSERT INTO Product_has_Category(categoryId, productId) VALUES (%s, %s);", project_data)
        self.db.commit()

    def get_category_id_name(self):
        add_product = ("SELECT * FROM Category")
        self.cursor.execute(add_product)
        return self.cursor.fetchall()

    def get_product(self, name):
        self.cursor.execute("SELECT * FROM Product WHERE product_name = (%s)", (name,))
        id_product = self.cursor.fetchall()[0][0]
        return id_product

    def get_substitut(self):
        self.cursor.execute("SELECT * FROM Substitute")
        lst = self.cursor.fetchall()
        return lst

    def get_product_by_category(self, category_id):
        self.cursor.execute("SELECT ProductId FROM Product_has_Category WHERE categoryId = (%s);", (category_id,))
        lst = list(self.cursor.fetchall()[:10])
        ret = []
        for i in lst:
            self.cursor.execute("SELECT * FROM Product WHERE ProductId = (%s)", (i[0],))
            ret.append(self.cursor.fetchone())
        return ret

    def save_product_substitut(self, productId, subsitute):
        project_data = (productId, subsitute)
        self.cursor.execute("INSERT INTO Substitute(productId, subsitute) VALUES (%s, %s);", project_data)
        self.db.commit()

    def get_product_substitue(self, id):
        self.cursor.execute("SELECT * FROM Product WHERE productId = (%s)", (id,))
        substitute = self.cursor.fetchall()[0][1]
        return substitute

    def get_all_substitute(self, lst):
        return [self.get_product_substitue(x[1]) for x in lst]

    def delete_product_substitute(self, id):
        self.cursor.execute("DELETE FROM Substitute WHERE substituteID = (%s)", (id,))
        self.db.commit()

    def delete_all_data_off(self):
        self.cursor.execute("DELETE FROM Substitute")
        self.cursor.execute("DELETE FROM Product_has_Category")
        self.cursor.execute("DELETE FROM Product")
        self.cursor.execute("DELETE FROM Category")
        self.db.commit()



# TODO 1 : Importer la base de donnée et faire la suite
# TODO 2 : AFFICHER LA LISTE DES SUBSITUT
# TODO 3 : REPOSER LA QUESTION AU CLIENT
# TODO 4 : FLAKE8 (LIBRAIRIE PYTHON POUR LA VERIFICATION DE LA PEP8)
# TODO 5 : DOCSTRING
