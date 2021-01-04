import mysql.connector


class DbOpenFoodFacts:
    """Connect db local"""
    CATEGORY_SIZE = 11
    PRODUCT_SIZE = 51

    def __init__(self):
        self.db = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='rootroot',
            auth_plugin='mysql_native_password',
            database='test_off_v1',
            charset='utf8')
        self.cursor = self.db.cursor()

    def save_category(self, lst_category):
        for i in range(1, self.CATEGORY_SIZE):
            add_category = ("INSERT INTO Category (name) VALUES (%s)")
            self.cursor.execute(add_category, (lst_category[i],))
            self.db.commit()

    def save_p(self, lst_product):
        add_product = ("INSERT INTO Product (product_name, nutrition_grades, ingredients_text, nova_groups_tags,"
                       " ingredients, product_url, magasin) VALUES (%s, %s, %s, %s, %s, %s, %s)")

        tuple_data = (lst_product[0], lst_product[1], lst_product[2][:50], "", "", lst_product[5],
                      lst_product[6])
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

    def get_substitut(self, name):
        self.cursor.execute("SELECT * FROM Substitue")
        lst = self.self.cursor.fetchall()
        return lst

    def get_product_by_category(self, category_id):
        self.cursor.execute("SELECT ProductId FROM Product_has_Category WHERE categoryId = (%s);", (category_id,))
        lst = list(self.cursor.fetchall()[:10])
        ret = []
        for i in lst:
            self.cursor.execute("SELECT * FROM Product WHERE ProductId = (%s)", (i[0],))
            ret.append(self.cursor.fetchone())
        # print(lst)
        # self.cursor.executemany("SELECT * FROM Product WHERE ProductId = (%s)", (lst,))
        return ret

    def save_product_substitut(self, productId, subsitute):
        project_data = (productId, subsitute)
        self.cursor.execute("INSERT INTO Substitute(productId, subsitute) VALUES (%s, %s);", project_data)
        self.db.commit()
