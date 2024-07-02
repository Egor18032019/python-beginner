import mysql.connector

mybd = mysql.connector.connect(
    # host="127.0.0.1",
    host="localhost",
    # host="0.0.0.0",
    port="3306",
    user="user",
    password="password",
    database="db"
)
myCur = mybd.cursor()
# sql = "CREATE DATABASE `python-example`"
# sql = "SHOW DATABASES"
# sql = "CREATE TABLE users (name VARCHAR(255), age INTEGER(3))"
sql = "SHOW TABLES"
myCur.execute(sql)

for el in myCur:
    print(el)

print("Мы поключены к: ", mybd)
