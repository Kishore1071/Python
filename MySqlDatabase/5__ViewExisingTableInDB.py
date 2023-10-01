import mysql.connector

mysql_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database="test_db"
)

mysql_cursor = mysql_db.cursor()

mysql_cursor.execute("show tables")

for tables in mysql_cursor:

    print(tables)