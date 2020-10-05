import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="rootroot",
    auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
for i in mycursor:
    print(i)
