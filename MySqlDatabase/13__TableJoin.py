import mysql.connector

mysql_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database="mydatabase"
)

mysql_cursor = mysql_db.cursor()

# mysql_cursor.execute("create table products (id int auto_increment primary key , product_name varchar(255), code varchar(255), price float, customer_id int)")

mysql_cursor.execute("select customers.name as customer_name, products.product_name as product_name from products inner join customers on products.customer_id = customers.id")

data = mysql_cursor.fetchall()

for x in data:

    print(x)