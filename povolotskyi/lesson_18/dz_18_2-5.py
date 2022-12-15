import mysql.connector



mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ro8e7ni4",
    database="my_first_db"
)

mycursor = mydb.cursor()

# dz_18_2
# mycursor.execute("CREATE TABLE student (id INT, name VARCHAR(255))")

# dz_18_3
# mycursor.execute("CREATE TABLE employee (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), salary INT(6))")

# dz_18_4
# mycursor.execute("ALTER TABLE student ADD PRIMARY KEY (id)")

# dz_18_5
sql = "INSERT INTO student (id, name) VALUES (%s, %s)"
val = ("01", "John")
mycursor.execute(sql, val)

mydb.commit()
print(mycursor.rowcount, "record inserted.")

sql = "INSERT INTO employee (name, salary) VALUES (%s, %s)"
val = ("John", "10000")
mycursor.execute(sql, val)

mydb.commit()
print(mycursor.rowcount, "record inserted.")