import mysql.connector

mysql_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database="mydatabase"
)

mysql_cursor = mysql_db.cursor()

mysql_cursor.execute("select * from customers order by name")  # Asending

"""
mysql_cursor.execute("select * from customers order by name desc") # Desending

"""

sorted_data = mysql_cursor.fetchall()

for data in sorted_data:

    print(data)