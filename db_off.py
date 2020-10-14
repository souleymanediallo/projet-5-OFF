import requests
import mysql.connector


class DbOpenFoodFacts:
    CATEGORY_SIZE = 11

    def __init__(self):
        self.db = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='rootroot',
            auth_plugin='mysql_native_password',
            database='test_off_v1',
            charset='utf8')
        self.cursor = self.db.cursor()

    # def save_category(self, lst_category):
    #     for i in range(1, self.CATEGORY_SIZE):
    #         add_category = (
    #             "INSERT INTO Category (categoryId, name) VALUES (%s, %s)")
    #         print(add_category)
    #         self.cursor.execute(add_category, (13, lst_category[i],))
    #         self.db.commit()

    def read_category(self):
        self.cursor.execute("SELECT * FROM Category")
        result = self.cursor.fetchall()
        print("-----------------------------------------------")
        print("| ID | LIST CATEGORIES                        |")
        print("-----------------------------------------------")
        for row in result:
            print(f"| {row[0]}    |   {row[1]}    |")
            print("-----------------------------------------------")
        print("-----------------------------------------------")

    def update_category(self):
        my_sql = "UPDATE Category SET name = 'Modifier ma category' WHERE categoryId = 12"
        self.cursor.execute(my_sql)
        self.db.commit()

    def delete_category(self):
        my_sql = "DELETE FROM Category WHERE categoryId = 3000"
        self.cursor.execute(my_sql)
        self.db.commit()
