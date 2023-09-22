import mysql.connector

mysql_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database="mydatabase"
)

mysql_cursor = mysql_db.cursor()

mysql_cursor.execute("select customers.name as customer_name, products.product_name as product_name from products inner join customers on products.customer_id = customers.id")

data = mysql_cursor.fetchall()

for x in data:

    print(x)