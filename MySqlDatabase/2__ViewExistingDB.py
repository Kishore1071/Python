import mysql.connector

mysql_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234"
)

mysql_cursor = mysql_db.cursor()

mysql_cursor.execute("show databases")

for dbs in mysql_cursor:

    print(dbs)