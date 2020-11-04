import requests
import mysql.connector


class DbOpenFoodFacts:
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
            
            add_category = (
                "INSERT INTO Category (name) VALUES (%s)")
    
            self.cursor.execute(add_category, (lst_category[i],))
            self.db.commit()

    def save_p(self, lst_product):
        
        add_product = ("INSERT INTO Product (product_name, nutrition_grades, ingredients_text, nova_groups_tags, ingredients, product_url, magasin) VALUES (%s, %s, %s, %s, %s, %s, %s)")
            # print(lst_product[i])
            # print(lst_product[i][0])
            # print(lst_product[i][1])
            # print(lst_product[i][2])
            # print(lst_product[i][3])
            # print(lst_product[i][4])
            # print(lst_product[i][5])
            # print(lst_product[i][6])
        self.cursor.execute(add_product, (lst_product[0], "o", "d", "t", "q","c","s"))
        self.db.commit()

    def save_product_category(self, categoryId, productId):
        project_data = (categoryId, productId)
        self.cursor.execute("INSERT INTO Product_has_Category(categoryId, productId) VALUES (%s, %s)", project_data)
        
    def get_category_id_name(self):
        add_product = ("SELECT * FROM Category")
        self.cursor.execute(add_product)
        return self.cursor.fetchall()

    def get_product(self, name):
        print(name)
        self.cursor.execute("SELECT * FROM Product WHERE product_name = (%s)", (name,))
        id_product = self.cursor.fetchall()[0][0]
        return id_product



    


    # def read_category(self):
    #     self.cursor.execute("SELECT * FROM Category")
    #     result = self.cursor.fetchall()
    #     return result

    # def clear(self):
    #     self.cursor.execute("DROP TABLE Category, Product, Product_has_Category, Substitue")

