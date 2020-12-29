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
        self.cursor.execute(add_product, (lst_product[0], lst_product[1], "d", "t", "q", "c", "s"))
        self.db.commit()

    def save_product_category(self, categoryId, productId):
        project_data = (categoryId, productId)
        self.cursor.execute("INSERT INTO Product_has_Category(categoryId, productId) VALUES (%s, %s)", project_data)

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
        self.cursor.execute("SELECT ProductId FROM Product_has_Category WHERE categoryId = (%s)", (category_id,))
        lst = self.cursor.fetchall()[:10]
        ret = []  
        for i in lst:
            print(i)
            self.cursor.executemany("SELECT * FROM product WHERE ProductId = (%s)", (i,))
            ret.append(self.cursor.fetchone())
        print(ret)
        return ret


m = DbOpenFoodFacts()
m.get_product_by_category(13) 
