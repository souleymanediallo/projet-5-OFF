import requests
import mysql.connector


class DbOpenFoodFacts:
    CATEGORY_SIZE = 10

    def __init__(self):
        self.db = mysql.connector.connect(
            host='localhost', user='root', passwd='rootroot', database="BasededonneeOFF")
        self.cursor = self.db.cursor()

    def save_category(self, lst_category):
        for i in range(1, self.CATEGORY_SIZE):
            add_category = (
                "INSERT INTO Category (name) VALUES({})".format('lst_category[i]'))
            print(add_category)
            self.cursor.execute(add_category)
            self.db.commit()


#
# add_category = ( "INSERT INTO Category (category) VALUES({})".format(lst_category[i]))
