import mysql.connector

mysql_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database="mydatabase"
)

mysql_cursor = mysql_db.cursor()

mysql_cursor.execute("select * from customers where name = 'Kishore'")

filtered_data = mysql_cursor.fetchall()

for data in filtered_data:

    print(data)