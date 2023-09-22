import mysql.connector

mysql_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database="mydatabase"
)

mysql_cursor = mysql_db.cursor()

mysql_cursor.execute("update customers set name = 'Banner' where id = 5")

mysql_db.commit()

print(mysql_cursor.rowcount, "Updated rows count")