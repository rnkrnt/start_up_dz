import mysql.connector



mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ro8e7ni4"
)

mycursor = mydb.cursor()

# dz_18_1
mycursor.execute("CREATE DATABASE my_first_db")