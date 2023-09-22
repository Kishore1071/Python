import mysql.connector

mysql_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database="mydatabase"
)

mysql_cursor = mysql_db.cursor()

mysql_cursor.execute("drop table customers")

# To check with the existence

mysql_cursor.execute("drop table if exists customers")